import os
from tkinter import *
from tkinter import ttk
from time import sleep

class output:
    
    def __init__(self):
        
        self.set_window()

    
    
    def set_window(self):
        
        self.window = Tk()
        
        self.window.title("Bs.to Downloader")
        self.window.geometry('250x150') 
        
        self.window.update()
        
        self.label_header = ttk.Label(self.window, text="", borderwidth=2, relief="groove", padding=20)
        self.label_header.grid(column=1, row=1)
        
        self.label_static = ttk.Label(self.window, text="")
        self.label_static.grid(column=1, row=2)
        
        self.label_status = ttk.Label(self.window, text="")
        self.label_status.grid(column=1, row=3)
        
        self.window.update()




    def def_header(self, text):
        
        self.label_header['text'] = text
        self.label_header.grid()
        self.window.update()
    
    
    
    def static_text(self, text):
        
        self.label_static['text'] = text
        self.label_static.grid()
        self.window.update()
    
    
    
    def status(self, text):
        
        self.label_status['text'] = text
        self.label_status.grid()
        self.window.update()