import os

class output:
    
    def __init__(self):
        self.header = ""
        self.static_in = ""
    
    def def_header(self, text=""):
        
        if text != "":
            self.header = text
        
        os.system("cls")
        print(self.header,"\n")
    
    def static_text(self, text=""):
        
        if text != "":
            self.static_in = text
        
        os.system("cls")
        self.def_header()
        print(self.static_in)
    
    def status(self, text):
        
        os.system("cls")
        self.def_header()
        self.static_text()
        print("Status:",text)