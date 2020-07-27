from kafka import KafkaConsumer
import input_influxdb as influx
import input_mysql as mysql
import decode_function as dc
import sys

bootstrap_servers = ['localhost:9092']
topicName = 'test'
consumer = KafkaConsumer(topicName,
                         group_id='group_1',
                         bootstrap_servers=bootstrap_servers,
                         auto_offset_reset='earliest')

influx_client = influx.connect_influxdb('influx_server_ip')
mysql_client = mysql.connect_mysql('mysql_server_ip', 43306, 'user_id', 'password', 'db_name')


try:
    for msg in consumer:
        print("%s:%d:%d: key=%s value=%s"
              % (msg.topic, msg.partition, msg.offset, msg.key, msg.value))

        # decode topic & log data
        topic, new_log = dc.msg_decode(msg.topic), dc.msg_decode(msg.value)

        # insert data into influx db & mysql
        try:
            influx.insert_influxdb(influx_client, influx.to_json(topic, new_log))
        except Exception as error:
            print("influx db insert error -> ", error)
            
        try:
            mysql.insert_mysql(mysql_client, new_log)
        except Exception as error:
            print("MySQL insert error -> ", error)

except KeyboardInterrupt:
    sys.exit()

