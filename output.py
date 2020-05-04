import os
from tkinter import *
from tkinter import ttk

class output:
    
    def __init__(self, gui):
        
        self.gui = gui
        if self.gui != "off":
            self.set_window()
        else:
            self.header = ""
            self.text_episode = ""

    
    
    def set_window(self):
        
        self.window = Tk()
        
        self.window.title("Bs.to Downloader")
        self.window.geometry('500x500') 
        
        self.window.update()
        
        self.label_header = ttk.Label(self.window, text="Analysiere Serie...", borderwidth=2, relief="groove", padding=20)
        self.label_header.grid(column=1, row=1)
        
        self.label_episode = ttk.Label(self.window, text="Analysiere Serie...", borderwidth=2, relief="groove", padding=20)
        self.label_episode.grid(column=1, row=2)
        
        self.label_ready = ttk.Label(self.window, text="Bereite alles vor:", padding=20)
        self.label_ready.grid(column=2, row=1, padx=20, pady=20)
        
        self.label_link = ttk.Label(self.window, text="Hole Serie auf Bs.to:")
        self.label_link.grid(column=2, row=2)
        
        self.label_rec = ttk.Label(self.window, text="Recaptcha lösen:")
        self.label_rec.grid(column=2, row=3)
        
        self.label_video = ttk.Label(self.window, text="Hole Video Link:")
        self.label_video.grid(column=2, row=4)
        
        self.label_download = ttk.Label(self.window, text="Download-Status:")
        self.label_download.grid(column=2, row=5)
        
        
        
        self.label_link_ready = ttk.Label(self.window, text="/", padding=20)
        self.label_link_ready.grid(column=3, row=1, padx=20, pady=20)
        
        self.label_link_solve = ttk.Label(self.window, text="/", padding=20)
        self.label_link_solve.grid(column=3, row=2)
        
        self.label_rec_solve = ttk.Label(self.window, text="/", padding=20)
        self.label_rec_solve.grid(column=3, row=3)
        
        self.label_video_solve = ttk.Label(self.window, text="/", padding=20)
        self.label_video_solve.grid(column=3, row=4)
        
        self.label_download_solve = ttk.Label(self.window, text="/", padding=20)
        self.label_download_solve.grid(column=3, row=5)
        
        self.window.update()




    def def_header(self, text):
        
        if self.gui != "off":
        
            self.label_header['text'] = text
            self.label_header.grid()
            self.window.update()
        
        else:
        
            self.header = text
            print(self.header)
    
    
    
    def episode(self, text):
        
        if self.gui != "off":
        
            self.label_episode['text'] = text
            self.label_episode.grid()
            self.window.update()
        
        else:
            
            os.system("cls")
            self.text_episode = text
            print(self.header, "\n", self.text_episode)
    
    
    def ready(self, text):
        
        if self.gui != "off":
        
            self.label_link_ready['text'] = text
            self.label_link_ready.grid()
            self.window.update()
        
        else:
            
            os.system("cls")
            print(self.header, "\n", self.text_episode, "\n", "Firefox Session wurde erstellt")
    
    
    
    def hoster_link(self, text):
        
        if self.gui != "off":
        
            self.label_link_solve['text'] = text
            self.label_link_solve.grid()
            self.window.update()
        
        else:
            
            os.system("cls")
            print(self.header, "\n", self.text_episode, "\n", "Folge wurde gefunden")
    
    
    
    def recaptcha(self, text):
        
        if self.gui != "off":
        
            self.label_rec_solve['text'] = text
            self.label_rec_solve.grid()
            self.window.update()
        
        else:
            
            os.system("cls")
            print(self.header, "\n", self.text_episode, "\n", "Recaptcha wurde gelöst")
    
    
    def download(self, text):
        
        if self.gui != "off":
        
            self.label_download_solve['text'] = text
            self.label_download_solve.grid()
            self.window.update()
    
    
    
    def video_link(self, text):
        
        if self.gui != "off":
        
            self.label_video_solve['text'] = text
            self.label_video_solve.grid()
            self.window.update()
        
        else:
            
            print("Download wird vorbereitet")