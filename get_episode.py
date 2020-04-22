from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class episode:
    
    def __init__(self, browser, link):
        
        self.browser = browser
        self.link = link
        self.session = 1
        self.erg = {}
        
    
    
    
    def get_episode(self):
        
        control = 0
        
        while control == 0:
            
            self.get_this()
            
            control = self.get_session()
        
        return self.erg

    
    
    
    def get_this(self):
        
        stop = 0
        counter_links = 1
        self.links = []
        
        while stop == 0:
            
            try:
                
                self.links.append(self.browser.find_element_by_xpath("(//table[@class='episodes']/tbody/tr[" + str(counter_links) + "]/td/a[2])").get_attribute("href"))
                
                counter_links += 1
            
            except:
                stop = 1
    
    
    
    
    def get_session(self):
        
        try:
            
            self.erg[self.session]=self.links
            self.session += 1
            self.browser.find_element_by_class_name('s' + str(self.session))
            self.browser.get(self.link + "/" + str(self.session))
            return 0
        
        except:
            return 1