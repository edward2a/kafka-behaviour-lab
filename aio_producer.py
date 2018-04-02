#!/usr/bin/env python3

from aiokafka import AIOKafkaProducer
import asyncio
import concurrent.futures
import random


class SendLoop(object):
    def __init__(self):
        # ev_loop
        self.loop = asyncio.get_event_loop()
        asyncio.set_event_loop(self.loop)

        # kafka producer
        self.producer = AIOKafkaProducer(
            loop=self.loop,
            bootstrap_servers='127.0.0.1:9092',
            value_serializer=None,
            max_batch_size=32768)

        self.start()

    def start(self):
        self.loop.run_until_complete(self.producer.start())
        asyncio.ensure_future(self.send_batch_loop())
        self.loop.run_forever()

    async def producer_start(self):
        await self.producer.start()

    async def send_one_loop(self):
        asyncio.ensure_future(self.send_one_loop())
        await self.producer.send('test', b'test message')

    async def send_batch_loop(self):
        asyncio.ensure_future(self.send_batch_loop())

        batch = self.producer.create_batch()
        for index in range(1024):
            batch.append(value=b'test message', key=None, timestamp=None)

        await self.producer.send_batch(batch, 'test', partition=random.choice(range(0,100)))


#async def executor():
#    await producer.start()
#    #loop = asyncio.get_event_loop()
#    loop.run_in_executor(pexecutor, send_one, producer)


workers = 2
with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as px:
    for worker in range(workers):
        px.submit(SendLoop)

#SendLoop()
