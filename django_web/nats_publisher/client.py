import json
from nats.aio.client import Client as NATS


async def send_message(subject, message):
    nc = NATS()
    await nc.connect("nats://nats:4222")
    if isinstance(message, dict):
        message = json.dumps(message)
    await nc.publish(subject, message.encode("utf-8"))
    await nc.close()
