from kafka import KafkaProducer

# broker IP
broker = ['localhost:9092']


# topic name 
topicName = 'test'


# generate producer object
producer = KafkaProducer(bootstrap_servers=broker)


# send message
producer.send(topicName, b'Hello kafka')
