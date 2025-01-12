import requests
from config import DOWNLOAD_PATH
import os

def handle_apk(bot, message, url):
    bot.reply_to(message, "Processing APK link...")
    apk_path = os.path.join(DOWNLOAD_PATH, "apk")
    os.makedirs(apk_path, exist_ok=True)

    try:
        response = requests.get(url)
        if response.status_code == 200:
            apk_file = os.path.join(apk_path, os.path.basename(url))
            with open(apk_file, 'wb') as file:
                file.write(response.content)
            bot.reply_to(message, "APK downloaded successfully.")
        else:
            bot.reply_to(message, "Failed to download APK.")
    except Exception as e:
        bot.reply_to(message, f"Error downloading APK: {e}")
