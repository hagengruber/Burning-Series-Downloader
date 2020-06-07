from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
from pydub import AudioSegment
from time import sleep
from convert import convert
import requests
import speech_recognition as sr
import os
from video_link import video
from output import output
from tqdm import tqdm

class recaptcha:
    """ Downloaded alle Folgen """
    
    def __init__(self, output):
        # Speichert Variablen
        
        self.output = output
    
    
    
    def trigger_recaptcha(self):
        
        # Klickt auf "Jetzt Abspielen"
        self.browser.find_element_by_class_name("hoster-player").click()
        # Popup wird vermutlich getriggert
        
        self.delete_tabs()
        
        # Trigger Recaptcha
        try:
            self.browser.find_element_by_class_name("hoster-player").click()
        except:
            r = 0
    
    
    
    
    def solve_recaptcha(self, browser):
        
        self.browser = browser
        self.trigger_recaptcha()
        
        try:
            self.browser.switch_to.frame(self.browser.find_elements_by_tag_name("iframe")[5])
        except:
            return 1
        
        self.recaptcha_wait("recaptcha-audio-button")
        
        try:
            self.browser.find_element_by_id("recaptcha-audio-button").click()
        except:
            return 1
        
        self.recaptcha_wait("audio-source")
        
        self.download_audio(self.browser.find_element_by_id("audio-source").get_attribute("src"))
        
        self.convert()
        
        text = self.speech_to_text()
        if text == 1:
            return 0
        
        self.solve_answer(text)
        
        return self.control()
    
    
    
    def get_browser(self):
        
        return self.browser
    
    
    def download_audio(self, audio):
        
        r = requests.get(audio)
        des = "audio.mp3"
        with open(des, 'wb') as f:
            f.write(r.content)
    
    
    
    def convert(self):
        
        c = convert()
        c.convert()
    
    
    def control(self):
        
        sleep(2)
        
        try:
            innerHTML = self.browser.find_element_by_class_name("rc-audiochallenge-error-message").get_attribute("innerHTML")
            if innerHTML == "":
                return 1
            else:
                return 0
        except Exception as e:
            return 1
    
    
    def recaptcha_wait(self, className):
        
        stop = 0
        
        while stop == 0:
            
            try:
                self.browser.find_element_by_id(className)
                stop = 1
            except Exception as e:
                # ToDo: Wenn zu viele Anfragen, beende Script
                self.get_final()
                sleep(3)
    
    
    
    
    def get_final(self):
        
        try:
            self.browser.find_element_by_class_name("rc-doscaptcha-header")
            show_error()
        except:
            return 0
    
    
    
    def show_error(self):
        
        self.output.recaptcha("Zu viele Anfragen")
        quit()
    
    
    
    
    
    def speech_to_text(self):
        
        r = sr.Recognizer()

        with sr.WavFile('audio.wav') as source:
            audio = r.record(source)

        try: 
            return r.recognize_google(audio, language='de-DE') 
            
        except sr.UnknownValueError:
            return 1

        except sr.RequestError as e: 
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            quit()
    
    
    
    def solve_answer(self, text):
        
        os.remove("audio.mp3")
        os.remove("audio.wav")
        
        self.browser.find_element_by_id("audio-response").send_keys(text)
        self.browser.find_element_by_id("recaptcha-verify-button").click()
    
    
    
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
                
                stop = 1
    
    
    
    
    def is_bs(self):
        
        try:
            
            if self.browser.find_element_by_class_name("fb-like").get_attribute("data-href") == "https://bs.to":
                return 1
            else:
                return 0
        except Exception as e:
            return 0