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
        #options.add_argument('--headless')
        #options.add_argument('--disable-gpu')
        
        try:
            # Versucht, Chrome Session zu erstellen
            self.browser = webdriver.Firefox(executable_path="geckodriver.exe", options=options)
            return self.browser
            
        except Exception as e:
            # Wenn dies fehlschlägt, gib Info aus
            self.output.status("Der Google Chrome Treiber wurde nicht gefunden...\nDownloade den passenden Treiber und verschiebe ihn mit dem Namen 'chromedriver.exe' in das aktuelle Verzeichnis\n\n")
            quit()