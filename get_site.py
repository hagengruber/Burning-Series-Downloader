from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class get_site:
    """ Holt BS Seite und prüft, ob Serie existiert """
    
    def __init__(self, link, browser):
        # Setzt Variablen
        
        self.link = link
        self.browser = browser
    
    
    
    def get_site(self):
        # Prüft, ob self.link eine korrekte Website ist
        
        try:
            self.browser.get(self.link)
        except:
            # Wenn nicht, gibt Fehlermeldung aus
            self.send_error_message()
            quit()
        
        # Prüft, ob Serie existiert
        return self.exist_serie()
    
    
    
    
    def exist_serie(self):
        # Prüft, ob Serie existiert
        
        try:
            # Versucht, ob Class serie existiert
            self.browser.find_element_by_class_name("serie")
            return self.browser
        
        except:
            # Wenn nicht, git Fehlermeldung aus
            self.send_error_message()
            quit()
    
    
    def send_error_message(self):
        
        print(self.link, "ist keine gültige BS-Seite")