import datetime
import mysql.connector


def connect_mysql(host_ip, port_num, user_id, pw, db):
    try:
        tmp = mysql.connector.connect(host=host_ip, port=port_num,
                                      user=user_id, password=pw,
                                      database=db)
    except Exception as error:
        print("MySQL connect fail -> ", error)

    return tmp.cursor()


def insert_mysql(cur, log_list):  # list type
    data = log_list.split()
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
    cur.execute(sql, val)



# create table
"""
cursor.execute(
    "CREATE TABLE "
    "test(date DATE, "
    "platform VARCHAR(10), "
    "user_ID VARCHAR(30), "
    "item VARCHAR(30), "
    "num INTEGER, "
    "price INTEGER, "
    "link VARCHAR(10))")
"""


"""
# insert example

cur = connect_mysql('localhost', 43306, 'jinung', 'Jinyes0410!', 'market')
insert_mysql(cur, generator_log.make_log())
"""
