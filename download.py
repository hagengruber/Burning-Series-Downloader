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
from output import output
from tqdm import tqdm

class download:
    """ Downloaded alle Folgen """
    
    def __init__(self, links, browser, output):
        # Speichert Variablen
        
        self.links = links
        self.browser = browser
        # Zählt alle Staffeln und Serien
        self.session = 1
        self.episode = 1
        self.video_Links = {}
        self.output = output
        self.output.def_header("Hole Download Links")
    
    
    
    def download(self):
        # main function
        
        # Solange nicht alle Staffeln abgearbeitet wurden
        while self.session <= len(self.links):
            
            # Downloaded alle Folgen einer Staffel
            
            self.video_Links[self.session] = self.get_site(self.links[self.session])
            
            self.session += 1
        
        self.download_form_link()
    
    
    
    
    
    def download_form_link(self):
        os.mkdir("Serie")
        session = 1
        
        for i,v in self.video_Links.items():
            os.mkdir("Serie/"+str(session))
            episode = 1
            print(i)
            for a,b in v.items():
                self.output.status("Downloade Folge " + str(episode) + " von Staffel " + str(session))
                des = "Serie/"+str(session)+"/"+str(episode)+".mp4"
                r = requests.get(b, stream=True)
                filelength = int(r.headers['Content-Length'])

                with open(des, 'wb') as f:
                    pbar = tqdm(total=int(filelength/1024))
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:                   # filter out keep-alive new chunks
                            pbar.update ()
                            f.write(chunk)
                episode += 1
        session += 1
    
    
    def get_site(self, links):
        # Downloaded alle Folgen einer Staffel
        
        # Solange nicht alle Folgen einer Staffel abgearbeitet worden sind
        episode = 1
        ep = {}
        for i in links:
            
            self.output.static_text("Staffel: "+str(self.session)+"\nFolge: "+str(episode))
            stop = 0
            
            while stop == 0:
                
                # Holt BS Link
                self.get_site_link(i)
                # Löst Recaptcha aus
                self.trigger_recaptcha()
                stop = self.solve_recaptcha()
                
                self.browser.switch_to.default_content()
            
            self.delete_tabs()
            
            ep[episode] = self.hoster()
            episode += 1
        
        return ep
    
    
    
    
    def get_site_link(self, link):
        
        self.browser.get(link)
    
    
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
    
    
    
    
    
    
    def solve_recaptcha(self):
        
        sleep(5)
        self.output.status("Versuche, Recaptcha zu lösen...")
        self.browser.switch_to.frame(self.browser.find_elements_by_tag_name("iframe")[5])
        
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
    
    
    
    
    def control(self):
        
        sleep(2)
        
        try:
            innerHTML = self.browser.find_element_by_class_name("rc-audiochallenge-error-message").get_attribute("innerHTML")
            if innerHTML == "":
                self.output.status("Recaptcha wurde gelöst")
                return 1
            else:
                self.output.status("Recaptcha wurde nicht gelöst... Wiederhole vorgang")
                return 0
        except Exception as e:
            self.output.status("Recaptcha wurde gelöst")
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
        
        self.output.status("Zu viele Anfragen des Recaptchas...")
        quit()
    
    
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
            self.output.status("Audio wurde nicht verstanden...")
            return 1

        except sr.RequestError as e: 
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            quit()
    
    
    
    def solve_answer(self, text):
        
        os.remove("audio.mp3")
        os.remove("audio.wav")
        
        self.browser.find_element_by_id("audio-response").send_keys(text)
        self.browser.find_element_by_id("recaptcha-verify-button").click()
    
    
    
    def hoster(self):
        
        d = video(self.browser, self.output)
        return d.download()
    
    
    
    def delete_tabs(self):
        self.output.status("Popups werden entfernt...")
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