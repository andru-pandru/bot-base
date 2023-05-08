import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['get_chat_id'])
def get_chat_id(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"The chat id is {chat_id}")
    print("chat_id is", chat_id)

bot.polling()
