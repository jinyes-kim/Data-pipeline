from influxdb import InfluxDBClient


def connect_influxdb(server_ip):
    try:
        client = InfluxDBClient(host=server_ip, port=8886)
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
                "user_id": user_id
            },
            "fields": {
                "item": item,
                "quantity": num,
                "price": price,
                "link": link
            }
        }
    ]
    return json_body


def insert_influxdb(client_var, json_data):
    client_var.write_points(json_data)


"""
# create db
client.create_database('test_db_name')

# switching db
client.switch_database('to_sue_db_name')
"""
