import telebot
import pymysql.cursors
import config

# Инициализация бота
bot = telebot.TeleBot(config.TOKEN)

# Функция для выполнения SQL-запросов
def execute_sql_command(sql_command):
    connection = pymysql.connect(
        host=config.mysqlhost,
        user=config.mysqluser,
        password=config.mysqlpassword,
        db=config.mysqldatabase
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_command)
            result = cursor.fetchall()
    except Exception as e:
        connection.rollback()
        print('Error executing SQL commands: {}'.format(e))
        result = None
    finally:
        connection.close()
    return result

# Считываем последнюю запись из базы данных и отправляем в Telegram
def send_last_record():
    # Выполняем SQL-запрос
    execute_sql_command("use bot_base")
    res = execute_sql_command("select task from tasks ORDER BY id DESC LIMIT 1")
    # Формируем сообщение
    result = '<b>' + str(res) + '</b>'
    # Отправляем сообщение в чат
    bot.send_message(config.chat_id, result, parse_mode='HTML')

# Выполняем отправку сообщения в Telegram
send_last_record()

