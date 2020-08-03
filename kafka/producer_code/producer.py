from kafka import KafkaProducer
import generator_log
import time

broker = ['localhost:9092']  # kafka broker ip
topicName = 'market'
producer = KafkaProducer(bootstrap_servers=broker)

count = 0

for _ in range(4990):
    count += 1
    input_data = generator_log.make_log()
    producer.send(topicName, input_data.encode())  # data ingestion
    time.sleep(0.2)
