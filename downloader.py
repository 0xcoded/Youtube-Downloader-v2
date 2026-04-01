import yt_dlp
import gui
import tkinter as tk
from tkinter import filedialog, messagebox

def descargar_video(url, only_audio, output_folder):
    if not output_folder:
        messagebox.showerror(title="ERROR", message="No seleccionaste carpeta")
        return

    """
    Descarga videos o playlists de YouTube en MP4 o MP3
    """

    opciones = {
        # 📁 Si es playlist, crea subcarpeta
        'outtmpl': f'{output_folder}/%(playlist_title)s/%(title)s.%(ext)s',
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',

        # 🔥 IMPORTANTE: permitir playlists
        'noplaylist': False,
        'ignoreerrors': True,  # continúa si un video falla
    }

    if only_audio:
        opciones.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        })

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])

        messagebox.showinfo(
            title="INFO",
            message="Descarga completada (video o lista)"
        )

    except Exception as e:
        messagebox.showerror(title="ERROR", message=f"Error al descargar: {e}")


if __name__ == "__main__":
    tk.messagebox.showinfo(title="Bienvenido", message="Collaboradores:\n0xcoded\nHanco89")
    root = tk.Tk()
    gui = gui.Gui(root)
    root.mainloop()
