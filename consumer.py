#!/usr/bin/env python3


import kafka
import signal

def count_info(signal, frame):
    print('messages collected: ' + str(x))

signal.signal(signal.SIGPOLL, count_info)

c = kafka.KafkaConsumer('test', bootstrap_servers='127.0.0.1:9092')
x = 0

try:
    print('Starting message polling...')
    while True: next(c); x += 1
except KeyboardInterrupt:
    print('Aborting...')
finally:
    c.close()
