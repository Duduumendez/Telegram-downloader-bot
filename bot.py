import telebot
from config import BOT_TOKEN, CHANNEL_USERNAME
from handlers.youtube_handler import handle_youtube_video, handle_youtube_audio
from handlers.social_handler import handle_social
from handlers.song_handler import handle_song
from handlers.apk_handler import handle_apk

bot = telebot.TeleBot(BOT_TOKEN)

# Function to check if the user is in the channel
def is_user_in_channel(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

# Start command
@bot.message_handler(commands=['start'])
def start(message):
    if is_user_in_channel(message.from_user.id):
        bot.reply_to(
            message,
            "Welcome to the Downloader Bot! Use the commands below to download:\n"
            "1. `/ytmp4 <YouTube link>` - Download YouTube Video (MP4)\n"
            "2. `/ytmp3 <YouTube link>` - Download YouTube Audio (MP3)\n"
            "3. `/insta <Instagram link>` - Download Instagram Post/Video\n"
            "4. `/tiktok <TikTok link>` - Download TikTok Video\n"
            "5. `/fb <Facebook link>` - Download Facebook Video\n"
            "6. `/song <Song name>` - Download Song (MP3)\n"
            "7. `/apk <App name>` - Download APK\n"
        )
    else:
        bot.reply_to(
            message,
            f"To continue, please join our Telegram channel: [Duduu Mendez Store]({CHANNEL_USERNAME})",
            parse_mode="Markdown",
        )

# Command handlers
@bot.message_handler(commands=['ytmp4'])
def download_yt_video(message):
    if is_user_in_channel(message.from_user.id):
        link = message.text.split(" ", 1)[1]
        handle_youtube_video(bot, message, link)
    else:
        bot.reply_to(message, "Please join the channel to use this feature.")

@bot.message_handler(commands=['ytmp3'])
def download_yt_audio(message):
    if is_user_in_channel(message.from_user.id):
        link = message.text.split(" ", 1)[1]
        handle_youtube_audio(bot, message, link)
    else:
        bot.reply_to(message, "Please join the channel to use this feature.")

@bot.message_handler(commands=['insta', 'tiktok', 'fb'])
def download_social_media(message):
    if is_user_in_channel(message.from_user.id):
        command, link = message.text.split(" ", 1)
        handle_social(bot, message, link, command)
    else:
        bot.reply_to(message, "Please join the channel to use this feature.")

@bot.message_handler(commands=['song'])
def download_song(message):
    if is_user_in_channel(message.from_user.id):
        song_name = message.text.split(" ", 1)[1]
        handle_song(bot, message, song_name)
    else:
        bot.reply_to(message, "Please join the channel to use this feature.")

@bot.message_handler(commands=['apk'])
def download_apk(message):
    if is_user_in_channel(message.from_user.id):
        app_name = message.text.split(" ", 1)[1]
        handle_apk(bot, message, app_name)
    else:
        bot.reply_to(message, "Please join the channel to use this feature.")

bot.polling(timeout=60, long_polling_timeout=60, non_stop=True)
