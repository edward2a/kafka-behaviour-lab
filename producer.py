#!/usr/bin/env python3


import kafka


p = kafka.KafkaProducer(bootstrap_servers='127.0.0.1:9092')
for i in range(10000):
    p.send('test', b'initialization message')

p.close()
