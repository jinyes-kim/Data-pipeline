# step 1 - download
- https://portal.influxdata.com/downloads/
- wget https://dl.influxdata.com/telegraf/releases/telegraf-1.14.5-1.x86_64.rpm
- sudo yum localinstall telegraf-1.14.5-1.x86_64.rpm

---

# step 2 - check conf file
- sudo vi telegraf.conf

---

# step 3 - start telegraf
- sudo systemctl start telegraf
- sudo systemctl restart telegraf

---

# step 4 - check status
- sudo journalctl -f -u telegraf.service
- sudo systemctl status telegraf

---

# step 5 - stop telegraf
- sudo systemctl stop telegraf

---

#### tip
- https://devconnected.com/how-to-setup-telegraf-influxdb-and-grafana-on-linux/
