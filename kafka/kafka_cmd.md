# kafka basic cmd

---

## 1. start cmd
#### step 1 - start zookeeper
- bin/zookeeper-server-start.sh -daemon config/zookeeper.properties


#### step 2 - start kafka broker
- bin/kafka-server-start.sh -daemon config/server.properties


#### step 3 - check log
- tail -f logs/*

---

## 2. stop cmd
#### step1 - stop kafka
- /bin/kafka-server-stop.sh


#### stop 2 - stop zookeeper
- /bin/zookeeper-server-stop.sh

---

## 3. control topic
#### generate topic
- ./kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3 --topic test

- (*test is sample topic name)



#### check topic list
- ./kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list


#### check consumer status
- ./kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group testgroup --describe

---

## 4. producer cmd
#### write message to broker using topic
- ./kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test

---

## 5. consumer cmd 
#### read message from broker using topic
- ./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning


#### read message from broker usig topic & group
- ./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test -group testgroup --from-beginning

- (* When use a topic group, the Consumer remember the last data and read it from then last message)

---

## 6. reset offset
#### to earliest is offset transform to zero
- ./kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group testgroup --topic test --reset-offsets --to-earliest --execute


#### can choice topic partition and offset number
- ./kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group testgroup --topic test:1 --reset-offsets --to-offset 2 --execute
