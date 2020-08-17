# pip install mysql-connector-python

import datetime
import mysql.connector
import generator_log

cnx = mysql.connector.connect(user='root', password='pw',
                              host='localhost', port=3306,
                              database='market')

cursor = cnx.cursor()

#cursor.execute("CREATE TABLE test(date DATE, platform VARCHAR(10), user_ID VARCHAR(30), item VARCHAR(30), num INTEGER, price INTEGER, link VARCHAR(10))")


def insert_sql(log_list):
    data = log_list
    data = data.split()
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    platform = data[0]
    user_id = data[1]
    item = data[2]
    num = int(data[3])
    price = int(data[4])
    link = data[5]
    sql = """INSERT INTO
                test(date, platform, user_id, item, num, price, link) 
                VALUES(%s, %s, %s, %s, %s, %s, %s)"""


    val = (time, platform, user_id, item, num, price, link)

    cursor.execute(sql, val)
    cnx.commit()

for _ in range(30):
    insert_sql(generator_log.make_log())


cursor.close()
