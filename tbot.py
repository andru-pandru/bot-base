#telebot
import pymysql.cursors
import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


def execute_sql_commands(sql_commands):

    connection = pymysql.connect(host=config.mysqlhost,
                                 user=config.mysqluser,
                                 password=config.mysqlpassword,
                                 db=config.mysqldatabase,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            for command in sql_commands:
                cursor.execute(command)

        connection.commit()

        # Fetch any remaining results
        with connection.cursor() as cursor:
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
print(execute_sql_commands("use botbase","select * from tasks"))



"""
def get_data(sql_commands):
    connection = pymysql.connect  (user=config.mysqluser,
                                password=config.mysqlpassword,
                                host=config.mysqlhost, 
                                database=config.mysqldatabase,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    
    print('1')
    
  #  sql_commands = ("use bot_base","select * from tasks")

    with connection.cursor() as cursor:
        for command in sql_commands:
            cursor.execute(command)
            data = cursor.fetchall()

    connection.close()
    bot.send_message(message.chat.id, data)
"""




@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/yodda.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id,"hello")


#run
bot.polling(none_stop=True)

