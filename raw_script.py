import mysql.connector
from datetime import datetime, date, time, timedelta
from mysql.connector import connect, Error
import csv

def get_dates():

    day_stop = datetime.today()
    day_start = (day_stop - timedelta(days=1)).replace(hour=00, minute=00, second=00)
    print(f'Day start: {day_start}\nDay stop:  {day_stop}')
    
    return ( day_start.strftime('%Y-%m-%d %H:%M:%S'), day_stop.strftime('%Y-%m-%d %H:%M:%S'))


days = get_dates()

sql_req = "SELECT * FROM calls WHERE start_time BETWEEN %s AND %s"
db_data = []

try:
    with connect(
        host="test_db.test",
        port="3306",
        user="admin",
        password="admin",
        database="history",
    ) as connection:
       
        with connection.cursor() as cursor:
            cursor.execute(sql_req, days)
            for db in cursor.fetchall():
                db_data.append(db)
                
except Error as e:
    print(e)

filename = f'req-{days[1].replace(":","-")}.csv'

output = open(filename, 'w', newline="")
with output:
    writer = csv.writer(output)
    writer.writerows(db_data)

print("done!")