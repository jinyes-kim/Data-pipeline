import datetime
import mysql.connector


def connect_mysql(host_ip, port_num, user_id, pw, db):
    try:
        tmp = mysql.connector.connect(host=host_ip, port=port_num,
                                      user=user_id, password=pw,
                                      database=db)
    except Exception as error:
        print("MySQL connect fail -> ", error)

    return tmp


def create_table(cursor, table_name):
    sql = "CREATE TABLE " + table_name + \
          " (date DATE, " \
          "platform VARCHAR(10), " \
          "user_ID VARCHAR(30), " \
          "item VARCHAR(30), " \
          "quantity INTEGER, " \
          "price INTEGER, " \
          "link VARCHAR(10))"
    cursor.execute(sql)


def insert_mysql(cursor, table_name, log_list):  # list type
    data = log_list
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    platform = data[0]
    user_id = data[1]
    item = data[2]
    quantity = int(data[3])
    price = int(data[4])
    link = data[5]

    sql = "INSERT INTO " + str(table_name) + \
          " (date, platform, user_id, item, quantity, price, link) " \
          "VALUES(%s, %s, %s, %s, %s, %s, %s)"
    val = (time, platform, user_id, item, quantity, price, link)
    cursor.execute(sql, val)
