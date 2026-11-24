
import telebot

bot = telebot.TeleBot 9234105884:AAFo8i4UKQkjoZb-kCppZuQLhyqVWD1hHPU

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Assalomu alaykum! AKA PREMIUM ga xush kelibsiz! ⭐")

bot.infinity_polling()
