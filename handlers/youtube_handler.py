import yt_dlp
import os
from config import DOWNLOAD_PATH

def handle_youtube(bot, message, url, format="mp4"):
    bot.reply_to(message, f"Processing YouTube {format.upper()} download...")
    youtube_path = os.path.join(DOWNLOAD_PATH, "youtube")
    os.makedirs(youtube_path, exist_ok=True)

    try:
        ydl_opts = {
            'format': 'bestaudio/best' if format == "mp3" else 'best',
            'outtmpl': f'{youtube_path}/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        with open(file_path, 'rb') as file:
            if format == "mp3":
                bot.send_audio(message.chat.id, file)
            else:
                bot.send_video(message.chat.id, file)
    except Exception as e:
        bot.reply_to(message, f"Error downloading YouTube {format.upper()}: {e}")
