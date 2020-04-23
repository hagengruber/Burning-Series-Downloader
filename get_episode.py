from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class episode:
    """ Speichert alle Folgen in einem Array """
    
    def __init__(self, browser, link):
        # Speichert alle Variablen
        
        self.browser = browser
        self.link = link
        self.session = 1
        self.erg = {}
        
    
    
    
    def get_episode(self):
        # Speichert alle Variablen
        
        # Solange nicht alle Staffeln abgearbeitet worden sind
        # Wenn control nicht 0 ist, existieren keine weiteren Staffeln mehr
        control = 0
        
        while control == 0:
            
            # Speichert in self.links alle Folgen einer Staffel
            self.get_this()
            
            # self.links wird in self.erg gespeichert
            # self.erg: {0:[links]}
            control = self.get_session()
        
        # Gib self.erg zurück
        return self.erg

    
    
    
    def get_this(self):
        # Speichert alle Folgen einer Staffel in self.links
        
        stop = 0
        counter_links = 1
        self.links = []
        
        while stop == 0:
            
            try:
                # Versuche, folge in self.links speichern
                self.links.append(self.browser.find_element_by_xpath("(//table[@class='episodes']/tbody/tr[" + str(counter_links) + "]/td[3]/a[1])").get_attribute("href"))
                
                counter_links += 1
            
            except:
                # Wenn keine Serie mehr existiert, brich Schleife ab
                stop = 1
    
    
    
    
    def get_session(self):
        # Versucht, nächste Staffel zu holen
        
        try:
            # Speichert self.links in dictonary self.erg
            self.erg[self.session]=self.links
            self.session += 1
            # Versuche, nächste Staffel zu holen
            self.browser.find_element_by_class_name('s' + str(self.session))
            self.browser.get(self.link + "/" + str(self.session))
            return 0
        
        except:
            # Wenn keine nächste Staffel existiert, brich Schleife ab
            return 1