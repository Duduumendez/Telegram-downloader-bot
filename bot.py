import telebot
from config import BOT_TOKEN
from handlers.youtube_handler import handle_youtube
from handlers.social_handler import handle_social
from handlers.apk_handler import handle_apk

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to the Downloader Bot! Send a link and choose:\n"
                          "1. YouTube Video/MP3\n"
                          "2. TikTok, Facebook, Instagram\n"
                          "3. APK File\n")

@bot.message_handler(content_types=['text'])
def handle_message(message):
    url = message.text
    if "youtube.com" in url or "youtu.be" in url:
        handle_youtube(bot, message, url)
    elif "tiktok.com" in url or "facebook.com" in url or "instagram.com" in url:
        handle_social(bot, message, url)
    elif url.endswith(".apk"):
        handle_apk(bot, message, url)
    else:
        bot.reply_to(message, "Unsupported link. Please provide a valid URL.")

if __name__ == '__main__':
    bot.polling()
