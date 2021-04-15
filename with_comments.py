# Тестовое задание для BP


# Подключаем нужные библиотеки
# Коннектор к MySQL для создания запросов
import mysql.connector

# Нам нужно получать дату и время сегодня для правильной выборки, так что подключаем их
# Беру дату, время и дельту для вычисления диапазона по ТЗ [2 дня]
from datetime import datetime, date, time, timedelta

# Чтобы проще писать код добавляем коннектор и лог ошибки отдельно
from mysql.connector import connect, Error

# Импортируем модуль для работы с CSV для вывода отчета
import csv



# Определяем и возвращаем дату начала нашей выборки и сегодня

# Вот тут возник очень большой вопрос к ТЗ - "за последние два дня"
# Его можно интерпретировать как за последние 2-е суток, или за последние 48 часов, и вывод будет отличатся
# Пример - если я сдею запрос в 15-го апреля в 00:10, какой результат должен быть?
#   а) Вывод звонков за 14 и 15-е апреля (последние 2-е суток), 
#   б) Вывод звонков за последние 48 часов - звонки за 13 апреля будут тк же учтены.
# Я сделал код для варианта а)

def get_dates():
    # Узнаем сегодняшнее число
    day_stop = datetime.today()
    # Узнаем число, с которого нам надо получить данные
    day_start = (day_stop - timedelta(days=1)).replace(hour=00, minute=00, second=00)

    # Пишем пользователю даты - чтобы не скучал)
    print(f'Day start: {day_start}\nDay stop:  {day_stop}')
    
    # Возвращаем тьюпл с датами, приведенными к формату в нашей MySQL-таблице
    return ( day_start.strftime('%Y-%m-%d %H:%M:%S'), day_stop.strftime('%Y-%m-%d %H:%M:%S'))


days = get_dates()

# Создаем запрос SQL с условием выбрать все, что между сегодня и условием, определенным в get_date
sql_req = "SELECT * FROM calls WHERE start_time BETWEEN %s AND %s"
db_data = []

# Подключаемся к базе
try:
    with connect(
        # Не забудьте сделать в hosts ОС запись
        host="test_db.test",
        port="3306",
        user="admin",
        password="admin",
        database="history",
    ) as connection:

        # С помощью коннектора достаем данные и циклом записываем их в предварительно созданный массив       
        with connection.cursor() as cursor:
            cursor.execute(sql_req, days)
            for db in cursor.fetchall():
                # Решил записать данные, вдруг они понадобятся для других операций
                db_data.append(db)
                
# Если что-то не так, эксепшн напишет нам об ошибке
except Error as e:
    print(e)

# сделаем название файла динамическим - оно будет содержать дату-время создания отчета
filename = f'req-{days[1].replace(":","-")}.csv'

# Создаем и записываем данные
output = open(filename, 'w', newline="")
with output:
    writer = csv.writer(output)
    writer.writerows(db_data)

print("done!")