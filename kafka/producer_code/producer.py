from kafka import KafkaProducer
import generator_log
import time

broker = ['broker_ip:9092']  # kafka broker ip
topicName = 'market'
producer = KafkaProducer(bootstrap_servers=broker)

for i, _ in enumerate(range(50)):
    input_data = generator_log.make_log()
    producer.send(topicName, input_data.encode())  # data ingestion
    time.sleep(0.2)

