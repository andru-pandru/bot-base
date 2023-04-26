#telebot
import telebot
import config


#with open('token.txt', 'r') as file:
#    TOKEN = file.read()

#print((TOKEN))

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open(static/welcom.webp, 'rb')
    bot.send_stiker(message.chat.id, sti)

    bot.send_message(message.chat.id, "hello, {0.first_name}!\n I am a </b>{1.first_name}</b> bot".format(message.from_user, bot.get_me()),parse_mode='html')


    


@bot.message_handler(content_types=['text'])

def msg(message):
    bot.send_message(message.chat.id, message.text)

#run
bot.polling(none_stop=True)

