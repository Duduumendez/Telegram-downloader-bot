import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN, CHANNEL_USERNAME
from handlers.youtube_handler import handle_youtube
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
    user_id = message.from_user.id
    if is_user_in_channel(user_id):
        bot.reply_to(
            message,
            "Welcome to the Downloader Bot! Use the commands below to download:\n"
            "1. `/ytmp4 <YouTube link>` - Download YouTube Video (MP4)\n"
            "2. `/ytmp3 <YouTube link>` - Download YouTube Audio (MP3)\n"
            "3. `/insta <Instagram link>` - Download Instagram Post/Video\n"
            "4. `/tiktok <TikTok link>` - Download TikTok Video\n"
            "5. `/fb <Facebook link>` - Download Facebook Video\n"
            "6. `/song <Song name>` - Download Song (MP3)\n"
            "7. `/apk <App name>` - Download APK\n",
            parse_mode="Markdown"
        )
    else:
        markup = InlineKeyboardMarkup()
        join_button = InlineKeyboardButton("JOIN", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")
        joined_button = InlineKeyboardButton("JOINED", callback_data="joined")
        markup.add(join_button, joined_button)
        bot.reply_to(
            message,
            f"To continue, please join our Telegram channel: [Duduu Mendez Store]({CHANNEL_USERNAME})",
            parse_mode="Markdown",
            reply_markup=markup
        )

# Callback for "Joined" button
@bot.callback_query_handler(func=lambda call: call.data == "joined")
def verify_joined(call):
    user_id = call.from_user.id
    if is_user_in_channel(user_id):
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text="Thank you for joining! Now you can use the bot.\n\n"
                 "Use the commands below to download:\n"
                 "1. `/ytmp4 <YouTube link>` - Download YouTube Video (MP4)\n"
                 "2. `/ytmp3 <YouTube link>` - Download YouTube Audio (MP3)\n"
                 "3. `/insta <Instagram link>` - Download Instagram Post/Video\n"
                 "4. `/tiktok <TikTok link>` - Download TikTok Video\n"
                 "5. `/fb <Facebook link>` - Download Facebook Video\n"
                 "6. `/song <Song name>` - Download Song (MP3)\n"
                 "7. `/apk <App name>` - Download APK\n",
            parse_mode="Markdown"
        )
    else:
        bot.answer_callback_query(call.id, "You haven't joined the channel yet. Please join and try again!")

# Command handlers
@bot.message_handler(commands=['ytmp4'])
def download_yt_video(message):
    if is_user_in_channel(message.from_user.id):
        try:
            link = message.text.split(" ", 1)[1]
            handle_youtube(bot, message, link, format="mp4")
        except IndexError:
            bot.reply_to(message, "Please provide a valid YouTube link.")
    else:
        bot.reply_to(message, "Please join the channel to use this feature.")

@bot.message_handler(commands=['ytmp3'])
def download_yt_audio(message):
    if is_user_in_channel(message.from_user.id):
        try:
            link = message.text.split(" ", 1)[1]
            handle_youtube(bot, message, link, format="mp3")
        except IndexError:
            bot.reply_to(message, "Please provide a valid YouTube link.")
    else:
        bot.reply_to(message, "Please join the channel to use this feature.")

@bot.message_handler(commands=['insta', 'tiktok', 'fb'])
def download_social_media(message):
    if is_user_in_channel(message.from_user.id):
        try:
            command, link = message.text.split(" ", 1)
            handle_social(bot, message, link, command)
        except IndexError:
            bot.reply_to(message, "Please provide a valid link.")
    else:
        bot.reply_to(message, "Please join the channel to use this feature.")

@bot.message_handler(commands=['song'])
def download_song(message):
    if is_user_in_channel(message.from_user.id):
        try:
            song_name = message.text.split(" ", 1)[1]
            handle_song(bot, message, song_name)
        except IndexError:
            bot.reply_to(message, "Please provide the name of the song.")
    else:
        bot.reply_to(message, "Please join the channel to use this feature.")

@bot.message_handler(commands=['apk'])
def download_apk(message):
    if is_user_in_channel(message.from_user.id):
        try:
            app_name = message.text.split(" ", 1)[1]
            handle_apk(bot, message, app_name)
        except IndexError:
            bot.reply_to(message, "Please provide the name of the APK.")
    else:
        bot.reply_to(message, "Please join the channel to use this feature.")

bot.polling(timeout=60, long_polling_timeout=60, non_stop=True)
