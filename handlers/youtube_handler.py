import yt_dlp
from config import DOWNLOAD_PATH
import os

def handle_youtube(bot, message, url):
    bot.reply_to(message, "Processing YouTube link...")
    video_path = os.path.join(DOWNLOAD_PATH, "youtube")
    os.makedirs(video_path, exist_ok=True)

    try:
        # Download video
        ydl_opts = {
            'outtmpl': f'{video_path}/%(title)s.%(ext)s',
            'format': 'best',  # Use 'bestaudio' for audio-only
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)
            bot.send_message(message.chat.id, f"Downloaded: {info['title']}")

        # Send video back to the user
        with open(file_path, 'rb') as video:
            bot.send_video(message.chat.id, video)

    except Exception as e:
        bot.reply_to(message, f"Error downloading YouTube video: {e}")
