#!/usr/bin/env python3


import kafka

p = kafka.KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])
while True:
    p.send('test', b'test message')
