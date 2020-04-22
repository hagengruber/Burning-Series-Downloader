from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
from pydub import AudioSegment
from time import sleep

class download:
    
    def __init__(self, links, browser):
        self.links = links
        self.browser = browser
        self.session = 1
        self.episode = 1
    
    
    
    def download(self):
        
        while self.session != len(self.links):
            self.get_site(self.links[self.session])
            self.session += 1
    
    
    
    
    def get_site(self, links):
        
        for i in links:
            self.get_site_link(i)
            self.disabled_recaptcha()
    
    
    
    def get_site_link(self, link):
        
        self.browser.get(link)
    
    
    
    
    def disabled_recaptcha(self):
        #ToDO: Weitermachen
        sleep(2)
        print("Klick")
        self.browser.find_element_by_class_name("hoster-player").click()
        sleep(5)
        print("Switch")
        self.browser.switch_to.window(self.browser.window_handles[0])
        print("Close")
        self.browser.close()
        print("Switch")
        self.browser.switch_to.window(self.browser.window_handles[0])
        sleep(5)
        print("Klick")
        self.browser.find_element_by_class_name("hoster-player").click()
        
        #self.browser.find_element_by_class_name("play").click()
        quit()