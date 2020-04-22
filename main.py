from chrome_session import session
from get_episode import episode
from download import download

class crawl:
    
    def __init__(self, link):
        # Setzt Variablen
        
        self.link = link
    
    
    def get_serie(self):
        # main function
        
        # Chrome Session erstellen
        self.create_session()
        
        # Seite Aufrufen
        self.get_site()
        
        # Erstellt einen Array mit den einzelnen Folgen
        self.get_episode()
        
        self.download()
    
    
    
    def create_session(self):
        # Erstelle Session
        
        s = session()
        self.browser = s.new_session()
    
    
    
    def get_site(self):
        # Holt Seite und prüft, ob Link korrekt war
        
        self.browser.get(self.link)
        
        # ToDo: Prüfen, ob Seite existiert
    
    
    
    def get_episode(self):
        
        e = episode(self.browser, self.link)
        self.links = e.get_episode()
    
    
    
    
    def download(self):
        
        d = download(self.links, self.browser)
        d.download()