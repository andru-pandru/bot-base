#telebot
import telegram
from telegram.ext import Updater, CommandHandler

bot = telegram.Bot(token='5352998015:AAH_st69lxHb3EMf0AnqLjhLWB_gDFAEsDo')

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello")

start_handler = CommandHandler('start', start)
