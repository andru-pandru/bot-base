#telebot
import pymysql.cursors
import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


def execute_sql_command(sql_command):

    connection = pymysql.connect(host=config.mysqlhost,
                                 user=config.mysqluser,
                                 password=config.mysqlpassword,
                                 db=config.mysqldatabase)

    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_command)
            result = cursor.fetchall()

    except Exception as e:
        # Roll back the transaction 
        connection.rollback()
        print('Error executing SQL commands: {}'.format(e))
        result = None

    finally:
        connection.close()

    return result



@bot.message_handler(commands=['last'])
def base_init(message):
    execute_sql_command("use bot_base")
    res = execute_sql_command("select task from tasks ORDER BY id DESC LIMIT 1")
    result='<b>'+(str(res))+'</b>'
    print(result)
    bot.send_message(message.chat.id,result,parse_mode='HTML')
    #pic = execute_sql_command("select link from tasks order by id desc limit 1")
    picture = open('static/describe.jpg','rb')
    bot.send_photo(message.chat.id,picture)







@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/yodda.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id,"hello")


#run
bot.polling(none_stop=True)

