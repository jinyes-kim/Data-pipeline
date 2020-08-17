# step 1 - download 
- https://portal.influxdata.com/downloads/

- ex) centos
- ~]# wget https://dl.influxdata.com/influxdb/releases/influxdb-1.8.1.x86_64.rpm
- ~]# sudo yum localinstall influxdb-1.8.1.x86_64.rpm 

---

# step 2 - start service
- ~]# sudo service influxdb start

---

# step 3 - start DB
- ~]# sudo service influxdb start
- ~]# influx
- ~]# influx -precision rfc3339

---

# step 4 - basic cmd
- show databases
- use db_name
- show measurements
- create database DB
- insert "topic",tag1="sample1",tag2="sample2"　field1="dummy1", field2=8086, time(123124) # 시간 생략 가능

