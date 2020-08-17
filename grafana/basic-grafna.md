# step 1 - download
- https://grafana.com/grafana/download
- wget https://dl.grafana.com/oss/release/grafana-7.1.0-1.x86_64.rpm
- sudo yum install grafana-7.1.0-1.x86_64.rpm


---
# step 2 - start grafana
- sudo systemctl daemon-reload
- sudo systemctl start grafana-server
- sudo systemctl enable grafana-server

---

# step 3 - check status
- sudo systemctl status grafana-server

---

# step 4 - stop grafana
- sudo systemctl stop grafana-server ?

---

# step 5 - connect browser
- localhost:3000
