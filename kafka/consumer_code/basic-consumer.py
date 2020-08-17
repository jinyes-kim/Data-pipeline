import sys
from kafka import KafkaConsumer

# broker IP
broker = ['localhost:9092']


# topic name
topicName = 'test'


# generate consumer object
consumer = KafkaConsumer(topicName,
                         group_id='group_1',
                         bootstrap_servers=broker,
                         auto_offset_reset='earliest')


# read message from consumer object
try:
    for msg in consumer:
        print("%s:%d:%d: key=%s value=%s" % (
            msg.topic, msg.partition, msg.offset, msg.key, msg.value))

except KeyboardInterrupt:
    sys.exit()
    
