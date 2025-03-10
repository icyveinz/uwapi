import asyncio
from faststream.nats import NatsBroker
import os

NATS_URL = os.getenv("NATS_URL", "nats://nats:4222")

broker = NatsBroker(NATS_URL)


@broker.subscriber("new.customer")
async def process_message(message: dict):
    print(f"Received message: {message}")


async def main():
    await broker.start()
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
