from firefox_session import session
from get_episode import episode
from download import download
from get_site import get_site

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
        
        # Downloaded alle Folgen
        self.download()
    
    
    
    def create_session(self):
        # Erstelle Session
        
        print("Erstelle Firefox Session...")
        s = session()
        self.browser = s.new_session()
        print("Session erstellt")
    
    
    
    def get_site(self):
        # Holt Seite und prüft, ob Link korrekt war
        
        print("Prüfe Link...")
        s = get_site(self.link, self.browser)
        self.browser = s.get_site()
        print("Serie gefunden")
    
    
    
    def get_episode(self):
        # Speichert alle Folgen in dictonary self.links
        
        print("Analysiere Staffeln und Folgen...")
        e = episode(self.browser, self.link)
        self.links = e.get_episode()
        print(len(self.links),"Staffel(n) gefunden")
    
    
    
    
    def download(self):
        # Downloaded alle Folgen
        
        print("Download wird gestartet...")
        d = download(self.links, self.browser)
        d.download()