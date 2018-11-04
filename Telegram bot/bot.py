import telebot

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

@bot.message_handler( commands=['start', 'go'] )
def start_handler(message):
    bot.send_message(message.chat.id, 'Hello')

if __name__ == '__main__':

    bot.polling()
