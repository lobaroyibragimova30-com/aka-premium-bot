
import telebot

bot = telebot.TeleBot("TOKEN_BU_YERGA")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Assalomu alaykum! AKA PREMIUM ga xush kelibsiz! ⭐")

bot.infinity_polling()
