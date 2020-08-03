from kafka import KafkaConsumer
import input_influxdb as influx
import input_mysql as mysql
import decode_function as dc
import sys
import datetime

bootstrap_servers = ['localhost:9092']
topicName = 'market'
consumer = KafkaConsumer(topicName,
                         group_id='group_1',
                         bootstrap_servers=bootstrap_servers,
                         auto_offset_reset='earliest')

try:
    influx_client = influx.connect_influxdb('influx_server_ip')
    influx_client.switch_database("market")
    print("connect influx DB")
except:
    print("connect fail - inlfux DB")

try:
    mysql_db = mysql.connect_mysql('mysql_server_ip', 3306, 'root', 'password', 'market')
    mysql_cursor = mysql_db.cursor()
    print("connect MySQL")
except:
    print("connect fail - MySQL")


# MySQL table check
mysql_table_list = []
mysql_cursor.execute("SHOW TABLES")
tables = mysql_cursor.fetchall()

for a in tables:
    word = str(a)
    if word not in mysql_table_list:
        mysql_table_list.append(word[2:-3])

# consume
try:
    for msg in consumer:
        print("%s:%d:%d: key=%s value=%s"
              % (msg.topic, msg.partition, msg.offset, msg.key, msg.value))

        # decode topic & log data
        topic, new_log = dc.msg_decode(msg.topic), dc.msg_decode(msg.value)

        # choose table
        table_name = datetime.datetime.now().strftime("%Y%m%d")  # table_name
        table_name = table_name + "_TB"

        if table_name not in mysql_table_list:
            mysql.create_table(mysql_cursor, table_name)
            mysql_table_list.append(table_name)

        # insert data into influx db & mysql
        try:
            influx_client.write_points(influx.to_json(topic, new_log))
        except Exception as error:
            print("influx db insert error -> ", error)

        try:
            mysql.insert_mysql(mysql_cursor, table_name, new_log)
            mysql_db.commit()
        except Exception as error:
            print("MySQL insert error -> ", error)

except KeyboardInterrupt:
    sys.exit()
