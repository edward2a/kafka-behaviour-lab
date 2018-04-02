#!/usr/bin/env python3

from aiokafka import AIOKafkaProducer
import asyncio
import concurrent.futures


class SendLoop(object):
    def __init__(self):
        # ev_loop
        self.loop = asyncio.get_event_loop()
        asyncio.set_event_loop(self.loop)

        # kafka producer
        self.producer = AIOKafkaProducer(loop=self.loop,bootstrap_servers='127.0.0.1:9092', value_serializer=None)
        self.start()

    def start(self):
        self.loop.run_until_complete(self.producer.start())
        asyncio.ensure_future(self.send_one_loop())
        self.loop.run_forever()

    async def producer_start(self):
        await self.producer.start()

    async def send_one_loop(self):
        asyncio.ensure_future(self.send_one_loop())
        await self.producer.send('test', b'test message')


#async def executor():
#    await producer.start()
#    #loop = asyncio.get_event_loop()
#    loop.run_in_executor(pexecutor, send_one, producer)


workers = 3
with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as px:
    for worker in range(workers):
        px.submit(SendLoop)

#SendLoop()
