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
            file_name = os.path.basename(url)
            file_path = os.path.join(apk_path, file_name)
            with open(file_path, 'wb') as file:
                file.write(response.content)
            bot.reply_to(message, "APK downloaded successfully.")

            # Send APK back to the user
            with open(file_path, 'rb') as apk:
                bot.send_document(message.chat.id, apk)
        else:
            bot.reply_to(message, "Failed to download APK.")

    except Exception as e:
        bot.reply_to(message, f"Error downloading APK: {e}")
