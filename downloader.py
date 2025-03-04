import yt_dlp

def download_video(url,solo_audio):
    output_folder = input("Ruta de descarga completa: ")
    opciones = {
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',  # Ruta de salida
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': "mp3",
        }] if solo_audio else None,
    }
    if solo_audio:
        opciones['format'] = 'bestaudio/best'  # Descarga solo audio
    else:
        opciones['format'] = 'bestvideo+bestaudio/best'  # Descarga video en la mejor calidad

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
            print(f"Descarga completada para: {url}")
    except Exception as e:
        print(f"Error al descargar: {e}")

if __name__=="__main__":
    url = input("Introduce la URL: ")
    format = input("¿Desea descargar sólo el audio? ")
    match format:
        case "s":
            download_video(url, True)
        case "n":
            download_video(url, False)
        case _:
            print("Respuesta inválida")