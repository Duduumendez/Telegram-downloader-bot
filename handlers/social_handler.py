import yt_dlp
import os
from config import DOWNLOAD_PATH

def handle_social(bot, message, url, command):
    bot.reply_to(message, f"Processing {command} link...")
    social_path = os.path.join(DOWNLOAD_PATH, command)
    os.makedirs(social_path, exist_ok=True)

    try:
        ydl_opts = {
            'outtmpl': f'{social_path}/%(title)s.%(ext)s',
            'format': 'best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        # Send video to the user
        with open(file_path, 'rb') as video:
            bot.send_video(message.chat.id, video)
    except Exception as e:
        bot.reply_to(message, f"Error downloading {command} video: {e}")
