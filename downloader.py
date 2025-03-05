import yt_dlp
import gui
import tkinter as tk
from tkinter import filedialog

def descargar_video(url, only_audio, output_folder):
    """
        Descarga un video de YouTube, con la opción de solo descargar el audio.

        Pide al usuario la ruta de descarga completa, y luego utiliza yt-dlp para
        descargar el video o audio en la mejor calidad posible.

        Si se elige solo el audio, lo descarga en formato mp3 con una calidad de
        192 kbps.
    """       
    opciones = {
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',  # Ruta de salida
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',  # Descargar en MP4
    }

    if only_audio:
        opciones.update({
            'format': 'bestaudio/best',  # Descarga solo el mejor audio
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',  # Calidad de audio
            }]
        })

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
            print(f"Descarga completada para: {url}")
    except Exception as e:
        print(f"Error al descargar: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = gui.Gui(root)
    root.mainloop()