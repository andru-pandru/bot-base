import pymysql.cursors
import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

def read_data_from_database():
    connection = pymysql.connect(host=config.mysqlhost,
                                 user=config.mysqluser,
                                 password=config.mysqlpassword,
                                 db=config.mysqldatabase)


    try:
        with connection.cursor() as cursor:
            sql_query = "SELECT task FROM tasks WHERE date_added = DATE_SUB(NOW(), INTERVAL 1 DAY)"
            cursor.execute(sql_query)
            result = cursor.fetchall()

    except Exception as e:
        connection.rollback()
        result = None

    finally:
        connection.close()

    return result


def send_to_telegram(data):
    

data = read_data_from_database()
send_to_telegram(data)
        
        
