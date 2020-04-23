from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class video:
    
    def __init__(self, browser):
        
        self.browser = browser
    
    
    
    def download(self):
        
        self.get_hoster()
    
    
    
    def get_hoster(self):
        
        hoster = ["vivo"]
        rHoster = "none"
        
        for i in hoster:
        
            if self.is_hoster(i) == 0:
                rHoster = i
        
        if rHoster != "none":
            print("Hoster:", rHoster)
        else:
            print("No Hoster found...")
    
    
    def is_hoster(self, hoster):
        
        try:
            
            self.browser.find_element_by_xpath("(//li[@class='active']/a/i[@class='hoster "+hoster+"'])")
            return 0
            
        except Exception as e:
            return 1