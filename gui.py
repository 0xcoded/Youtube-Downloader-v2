
import tkinter as tk
import os
from tkinter import filedialog
import downloader

class Gui:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Simple Youtube Downloader")
        self.parent.geometry("600x300")
        self.parent.resizable(False, False)
        self.parent.configure(bg="#333333")
        
     
        if os.name == "nt":
            self.parent.iconbitmap("interfaz/youtube.ico")
        else:
            self.parent.iconphoto(False, tk.PhotoImage(file = "interfaz/youtube.png"))
           
        self.title = tk.Label(   
            self.parent,
            text="Downloader Coded",
            font=("nunito", 24),
            fg= "#FF3737",
            bg = "#333333",
            padx= 30,
            pady= 30,
        )
        self.title.place(x = 120, y = 0 )
        
        
        self.title_url = tk.Label(
            self.parent,
            text="Ingrese la URL del video de YouTube:",
            font=("nunito", 16),
            fg= "#FF6666",
            bg = "#333333",
            padx= 30
        )
        self.title_url.place(x = 75, y = 110 )
    
        global url
        url = self.url_entry = tk.Entry(
            self.parent,
            font=("nunito", 16),
            fg= "#000000",
            bg = "#FFFFFF",
            width=30
        )
        self.url_entry.place(x = 110, y = 150 )
        
        self.download_button_mp4 = tk.Button(
            self.parent,
            text="Descargar MP4",
            font=("nunito", 16),
            fg= "#FFFFFF",
            bg = "#555555",
            command=download_mp4
        )
        self.download_button_mp4.place(x = 15, y = 225 )
        
        self.download_button_mp3 = tk.Button(
            self.parent,
            text="Descargar MP3",
            font=("nunito", 16),
            fg= "#FFFFFF",
            bg = "#555555",
            command=download_mp3
        )
        self.download_button_mp3.place(x = 230, y = 225 )
        
        self.exit_button = tk.Button(
            self.parent,
            text="Salir",
            font=("nunito", 16),
            fg= "#FFFFFF",
            bg = "#555555",
            command=exit,
            width = 10
        )
        self.exit_button.place(x = 450, y = 225 )


    
def download_mp3():
    tk.messagebox.showinfo(title="INFO", message="Iniciando descarga en MP3, espere...")
    downloader.descargar_video(url.get(), True, select_directory())
    
def download_mp4():
    tk.messagebox.showinfo(title="INFO", message="Iniciando descarga en MP4, espere...")
    downloader.descargar_video(url.get(), False, select_directory())
        
def select_directory():
        output_folder = filedialog.askdirectory()
        if not output_folder:
            return False
        return output_folder
        
       
        