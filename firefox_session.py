from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from output import output

class session:
    
    def __init__(self, output):
        
        self.output = output
    
    def new_session(self):
    
        # Erstellt Chrome Session
        
        # Window ist disabled
        options = webdriver.FirefoxOptions()
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')

        try:
            # Versucht, Chrome Session zu erstellen
            browser = webdriver.Firefox(executable_path="geckodriver.exe", options=options)
            
        except Exception as e:
            # Wenn dies fehlschlägt, gib Info aus
            print("Fehler beim Erstellen der Firefox Session")
            quit()
        
        return browser