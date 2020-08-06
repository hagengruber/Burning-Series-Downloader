from firefox_session import session
from get_episode import episode
from download import download
from get_site import get_site
from output import output
from time import sleep

class crawl:
    
    def __init__(self, link):
        # Setzt Variablen
        
        self.link = link
        self.session = 1
        self.gui = "on"
    
    
    
    
    
    def get_serie(self):
        # main function
        
        self.output = output(self.gui)
        
        self.output.ready("...")
        
        # Chrome Session erstellen
        self.create_session()
        
        # Seite Aufrufen
        self.get_site()
        
        # Erstellt einen Array mit den einzelnen Folgen
        self.get_episode()
        
        self.output.ready("ok")
        
        # Downloaded alle Folgen
        self.download()
        
        self.browser.quit()
    
    
    
    
    def create_session(self):
        # Erstelle Session
        
        s = session(self.output)
        self.browser = s.new_session()
        exit()
    
    
    
    def get_site(self):
        # Holt Seite und prüft, ob Link korrekt war
        
        s = get_site(self.link, self.browser)
        self.browser = s.get_site()
    
    
    
    def get_episode(self):
        # Speichert alle Folgen in dictonary self.links
        
        e = episode(self.browser, self.link)
        self.links = e.get_episode()
        #self.output.status(str(len(self.links))+"Staffel(n) gefunden")
    
    
    
    
    def download(self):
        # Downloaded alle Folgen
        
        d = download(self.links, self.browser, self.output, self.session)
        d.download()