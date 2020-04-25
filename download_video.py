from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from output import output

class video:
    
    def __init__(self, browser, output):
        
        self.browser = browser
        self.output = output
    
    
    
    def download(self):
        
        return self.get_hoster()
    
    
    
    def get_hoster(self):
        
        hoster = ["vivo"]
        rHoster = "none"
        
        for i in hoster:
        
            if self.is_hoster(i) == 0:
                rHoster = i
        
        if rHoster != "none":
            if rHoster == "vivo":
                return self.download_vivo()
        else:
            self.output.status("No Hoster found")
    
    
    def is_hoster(self, hoster):
        
        try:
            
            self.browser.find_element_by_xpath("(//li[@class='active']/a/i[@class='hoster "+hoster+"'])")
            return 0
            
        except Exception as e:
            return 1
    
    
    
    
    def download_vivo(self):
        
        self.output.status("Hole Video Link")
        self.browser.get(self.get_link())
        return self.play()
    
    
    
    def get_link(self):
        
        return self.browser.find_element_by_xpath("(//div[@class='hoster-player']/a)").get_attribute("href")
    
    
    
    def play(self):
        
        self.wait_video()
        self.output.status("Video Link gefunden")
        return self.browser.find_element_by_tag_name("source").get_attribute("src")
    
    
    
    
    def wait_video(self):
        
        stop = 0
        while stop == 0:
            
            try:
                self.browser.find_element_by_tag_name("source")
                stop = 1
            except Exception as e:
                sleep(2)
        
        sleep(3)
    
    
    
    def is_vivo(self):
        
        try:
            
            self.browser.find_element_by_class_name("container vivo-content-box-wrapper")
            return 1
        except Exception as e:
            return 0