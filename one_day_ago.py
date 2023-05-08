import pymysql.cursors
import telebot
import configimport pymysql.cursors
import telebot
import config


bot = telebot.TeleBot(config.TOKEN)

def base_init(message):
    execute_sql_command("use bot_base")
    res = execute_sql_command("select task from tasks ORDER BY id DESC LIMIT 1")
    result='<b>'+(str(res))+'</b>'
    print(result)
    bot.send_message(message.chat.id,result,parse_mode='HTML')
    #pic = execute_sql_command("select link from tasks order by id desc limit 1")
    picture = open('static/describe.jpg','rb')
    bot.send_photo(message.chat.id,picture)



