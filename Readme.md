# Log Analysis Using Hadoop (HDFS + YARN + MapReduce)

## 📌 Project Overview
This project demonstrates how large-scale log data can be processed using **Apache Hadoop**.  
A single-node Hadoop cluster was configured on Linux, and web server access logs were analyzed using **MapReduce running on YARN** with **Hadoop Streaming (Python)**.

The goal of the project is to count the number of requests coming from each IP address, simulating a real-world log analysis use case.

---

## 🛠️ Technologies Used
- Apache Hadoop 3.3.6
- HDFS (Hadoop Distributed File System)
- YARN (Yet Another Resource Negotiator)
- MapReduce
- Hadoop Streaming
- Python 3
- Linux (Kali Linux)

---

## 📂 Dataset
The dataset consists of web server access logs similar to Apache/Nginx logs.

**Sample log format:**
192.168.1.1 - - [30/Dec/2025:22:01:01] "GET /index.html HTTP/1.1" 200


✅ REQUIRED PERMISSIONS (VERY IMPORTANT)

Run once:

chmod +x mapper/mapper.py reducer/reducer.py

🚀 HOW IT RUNS IN HADOOP
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-files mapper/mapper.py,reducer/reducer.py \
-mapper mapper.py \
-reducer reducer.py \
-input /logs/input \
-output /logs/output



📊 SAMPLE OUTPUT (part-00000)
192.168.1.1    3
192.168.1.2    2
192.168.1.3    1

