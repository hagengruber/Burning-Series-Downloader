from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
from pydub import AudioSegment
from time import sleep
from convert import convert
import requests
import speech_recognition as sr
import os
from download_video import video

class download:
    """ Downloaded alle Folgen """
    
    def __init__(self, links, browser):
        # Speichert Variablen
        
        self.links = links
        self.browser = browser
        # Zählt alle Staffeln und Serien
        self.session = 1
        self.episode = 1
    
    
    
    def download(self):
        # main function
        
        # Solange nicht alle Staffeln abgearbeitet wurden
        while self.session <= len(self.links):
            
            # Downloaded alle Folgen einer Staffel
            self.get_site(self.links[self.session])
            quit()
            self.session += 1
    
    
    
    
    def get_site(self, links):
        # Downloaded alle Folgen einer Staffel
        
        # Solange nicht alle Folgen einer Staffel abgearbeitet worden sind
        for i in links:
            
            # Holt BS Link
            self.get_site_link(i)
            # Löst Recaptcha aus
            self.trigger_recaptcha()
            self.solve_recaptcha()
            
            self.browser.switch_to.default_content()
            
            self.delete_tabs()
            
            self.download_video()
            
            break
    
    
    
    def create_session(self):
        # Erstelle Session
        
        print("Erstelle Firefox Session...")
        s = session()
        self.browser = s.new_session()
        print("Session erstellt")
    
    
    def get_site_link(self, link):
        
        self.browser.get(link)
    
    
    def trigger_recaptcha(self):
        
        # Klickt auf "Jetzt Abspielen"
        self.browser.find_element_by_class_name("hoster-player").click()
        # Popup wird vermutlich getriggert
        
        self.delete_tabs()
        
        # Trigger Recaptcha
        self.browser.find_element_by_class_name("hoster-player").click()
    
    
    
    def remove_popup(self):
        
        self.browser.switch_to.window(self.browser.window_handles[0])
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])
    
    
    
    
    def solve_recaptcha(self):
        
        sleep(5)
        self.browser.switch_to.frame(self.browser.find_elements_by_tag_name("iframe")[5])
        
        self.recaptcha_wait("recaptcha-audio-button")
        
        self.browser.find_element_by_id("recaptcha-audio-button").click()
        
        self.recaptcha_wait("audio-source")
        
        self.download_audio(self.browser.find_element_by_id("audio-source").get_attribute("src"))
        
        self.convert()
        
        text = self.speech_to_text()
        
        self.solve_answer(text)
    
    
    
    def recaptcha_wait(self, className):
        
        stop = 0
        
        while stop == 0:
            
            try:
                self.browser.find_element_by_id(className)
                stop = 1
            except Exception as e:
                print(e)
                sleep(3)
    
    
    
    def download_audio(self, audio):
        
        r = requests.get(audio)
        des = "audio.mp3"
        with open(des, 'wb') as f:
            f.write(r.content)
    
    
    
    def convert(self):
        
        c = convert()
        c.convert()
    
    
    
    def speech_to_text(self):
        
        r = sr.Recognizer()

        with sr.WavFile('audio.wav') as source:
            audio = r.record(source)

        try: 
            return r.recognize_google(audio, language='de-DE') 
        
        except sr.UnknownValueError: 
            print("Google Speech Recognition could not understand audio")
            quit()

        except sr.RequestError as e: 
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            quit()
    
    
    
    def solve_answer(self, text):
        
        os.remove("audio.mp3")
        os.remove("audio.wav")
        
        self.browser.find_element_by_id("audio-response").send_keys(text)
        self.browser.find_element_by_id("recaptcha-verify-button").click()
    
    
    
    def download_video(self):
        
        d = video(self.browser)
        d.download()
    
    
    
    def delete_tabs(self):
        stop = 0
        counter = 0
        while stop == 0:
            
            try:
                
                self.browser.switch_to.window(self.browser.window_handles[counter])
                sleep(2)
                control = self.is_bs()
                
                if control == 1:
                    counter += 1
                    
                else:
                    self.browser.close()
                    counter = 0
                    
            except Exception as e:
                print("Fehler:",e)
                
                stop = 1
    
    
    
    
    def is_bs(self):
        
        try:
            
            if self.browser.find_element_by_class_name("fb-like").get_attribute("data-href") == "https://bs.to":
                return 1
            else:
                return 0
        except Exception as e:
            print("Fehler:",e)
            return 0