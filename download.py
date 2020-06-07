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
from recaptcha import recaptcha
import os.path

class download:
    """ Downloaded alle Folgen """
    
    def __init__(self, links, browser, output, session):
        # Speichert Variablen
        
        self.links = links
        self.browser = browser
        # Zählt alle Staffeln und Serien
        self.session = session
        self.episode = 1
        self.video_Links = {}
        self.output = output
        self.output.def_header("Hole Download Links")
        self.name = self.get_name().replace("|", "")
        self.output.def_header(self.name)
    


    def get_name(self):
        
        element = self.browser.find_elements_by_tag_name("small")[0]
        self.browser.execute_script(" var element = arguments[0]; element.parentNode.removeChild(element); ", element)
        
        return self.browser.find_elements_by_tag_name("h2")[0].get_attribute("innerHTML").strip()





    def download(self):
        # main function
        
        try:
            os.mkdir(self.name)
        except:
            self.set_session()
            
        for i,b in self.links.items():
            
            if self.session == i:
                
                if not os.path.isdir(self.name + "/" + str(self.session)):
                    os.mkdir(self.name + "/" + str(self.session))
                
                while self.episode <= len(b):
                    
                    self.output.hoster_link("...")
                    
                    self.download_from_src(self.get_site(self.links[self.session]))
                    self.episode += 1
                
                self.episode = 1
                self.session += 1
    
    
    
    def set_session(self):
        
        for a,b in self.links.items():
        
            if os.path.isdir(self.name + "/" + str(a)):
                
                count = 1
                
                for c in b:
                    if os.path.isfile(self.name + "/" + str(a) + "/" + str(count) + ".mp4"):
                        count += 1
                    else:
                        self.episode = count
                        
                        return 0
                
            else:
                
                if not self.session > a:
                    
                
                    self.session = a
                    self.episode = 1
                    return 0
    
    
    def download_from_src(self, link):
        
        self.output.download("...")
        
        des = self.name + "/" + str(self.session) + "/" + str(self.episode) + ".mp4"
        
        r = requests.get(link, stream=True)
        
        filelength = int(r.headers['Content-Length'])

        #self.output.static_text("Downloade Folge " + str(self.episode) + " von Staffel " + str(self.session))

        with open(des, 'wb') as f:
            
            pbar = tqdm(total=int(filelength/1024))
            
            for chunk in r.iter_content(chunk_size=1024):
                
                if chunk:
                    
                    pbar.update()
                    self.output.download(str(pbar).split("|")[0].strip())
                    
                    f.write(chunk)
    
    
    
    
    
    def get_site(self, links):
        # Downloaded alle Folgen einer Staffel
        
        self.output.episode("Staffel: "+str(self.session)+"\nFolge: "+str(self.episode))
        stop = 0
        
        s = recaptcha(self.output)
        
        while stop == 0:
            
            # Holt BS Link
            
            self.get_site_link(links[self.episode-1])
            
            self.output.hoster_link("ok")
            
            self.output.recaptcha("...")
            
            # Löst Recaptcha aus
            
            stop = s.solve_recaptcha(self.browser)
            
        self.browser = s.get_browser()
        self.browser.switch_to.default_content()
        self.delete_tabs()
        
        self.output.recaptcha("ok")
        
        return self.get_links()
    
    
    
    def get_site_link(self, link):
        
        self.browser.get(link)
    
    
    
    
    
    def get_links(self):
        
        d = video(self.browser, self.output)
        return d.get_video()
    
    
    
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