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

    result = "uuups"

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM tasks")
            result = cursor.fetchall()
            
            for row in result:
                print(row)

    except Exception as e:
        # Roll back the transaction 
        connection.rollback()
        print('Error executing SQL commands: {}'.format(e))
        result = None

    finally:
        connection.close()

    return result



@bot.message_handler(commands=['last'])
def base_init(none):
    execute_sql_command("use bot_base")
    result = execute_sql_command("select * from tasks")

    print(result)





@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/yodda.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id,"hello")


#run
bot.polling(none_stop=True)

