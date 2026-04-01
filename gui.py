import tkinter as tk
import os
from tkinter import filedialog, messagebox
import downloader


class Gui:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Simple Youtube Downloader")
        self.parent.geometry("600x300")
        self.parent.resizable(False, False)
        self.parent.configure(bg="#333333")

        # Icono
        if os.name == "nt":
            self.parent.iconbitmap("interfaz/youtube.ico")
        else:
            self.parent.iconphoto(False, tk.PhotoImage(file="interfaz/youtube.png"))

        # Título principal
        self.title = tk.Label(
            self.parent,
            text="Downloader Coded",
            font=("nunito", 24),
            fg="#FF3737",
            bg="#333333",
            padx=30,
            pady=30,
        )
        self.title.place(x=120, y=0)

        # Texto URL
        self.title_url = tk.Label(
            self.parent,
            text="Ingrese la URL (video o playlist):",
            font=("nunito", 16),
            fg="#FF6666",
            bg="#333333",
            padx=30
        )
        self.title_url.place(x=75, y=110)

        # Input URL
        self.url_entry = tk.Entry(
            self.parent,
            font=("nunito", 16),
            fg="#000000",
            bg="#FFFFFF",
            width=30
        )
        self.url_entry.place(x=110, y=150)

        # Botón MP4
        self.download_button_mp4 = tk.Button(
            self.parent,
            text="Descargar MP4",
            font=("nunito", 16),
            fg="#FFFFFF",
            bg="#555555",
            command=self.download_mp4
        )
        self.download_button_mp4.place(x=15, y=225)

        # Botón MP3
        self.download_button_mp3 = tk.Button(
            self.parent,
            text="Descargar MP3",
            font=("nunito", 16),
            fg="#FFFFFF",
            bg="#555555",
            command=self.download_mp3
        )
        self.download_button_mp3.place(x=230, y=225)

        # Botón salir
        self.exit_button = tk.Button(
            self.parent,
            text="Salir",
            font=("nunito", 16),
            fg="#FFFFFF",
            bg="#555555",
            command=self.parent.quit,
            width=10
        )
        self.exit_button.place(x=450, y=225)

    # -------------------------
    # FUNCIONES
    # -------------------------

    def download_mp3(self):
        url = self.url_entry.get().strip()

        if not url:
            messagebox.showerror("Error", "Introduce una URL")
            return

        folder = self.select_directory()
        if not folder:
            return

        messagebox.showinfo("INFO", "Iniciando descarga en MP3...")
        downloader.descargar_video(url, True, folder)

    def download_mp4(self):
        url = self.url_entry.get().strip()

        if not url:
            messagebox.showerror("Error", "Introduce una URL")
            return

        folder = self.select_directory()
        if not folder:
            return

        messagebox.showinfo("INFO", "Iniciando descarga en MP4...")
        downloader.descargar_video(url, False, folder)

    def select_directory(self):
        folder = filedialog.askdirectory(title="Selecciona carpeta de descarga")
        return folder if folder else None
