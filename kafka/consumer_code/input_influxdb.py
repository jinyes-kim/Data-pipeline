from influxdb import InfluxDBClient
import datetime

def connect_influxdb(server_ip):
    try:
        client = InfluxDBClient(host=server_ip, port=8086)
    except Exception as error:
        print("influx db connect fail -> ", error)
    return client


def to_json(topic, data):
    data = data.split()
    platform = data[0]
    user_id = data[1]
    item = data[2]
    num = data[3]
    price = data[4]
    link = data[5]

    json_body = [
        {
            "measurement": topic,
            "tags": {
                "platform": platform,
                "link": link
            },
            "fields": {
                "user_id": user_id,
                "item": item,
                "quantity": num,
                "price": price,
            }
            #"time":  datetime.datetime.now()
        }
    ]
    return json_body

