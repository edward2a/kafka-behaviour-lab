#!/usr/bin/env python3


import confluent_kafka as kafka


p = kafka.Producer({'bootstrap.servers':'127.0.0.1:9092'})

while True:
    try:
        p.produce('test', b'test message')
    except BufferError:
        print('--> buffer flush')
        p.flush()
        continue
