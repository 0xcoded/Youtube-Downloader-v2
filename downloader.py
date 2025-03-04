import yt_dlp

def download_video(url,only_audio):
    output_folder = input("Ruta de descarga completa: ")
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

if __name__=="__main__":
    url = input("Introduce la URL: ")
    format = input("¿Desea descargar sólo el audio? s/n ")
    match format:
        case "s":
            download_video(url, True)
        case "n":
            download_video(url, False)
        case _:
            print("Respuesta inválida")
