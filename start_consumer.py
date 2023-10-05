import asyncio
import logging.config

from src.services import controller


async def consume_messages():
    logger = logging.getLogger("Consumer")
    consumer = controller.kafka
    logger.info("Starting Consumer")

    while True:
        await consumer.get_message(topic="parse")


if __name__ == "__main__":
    asyncio.run(consume_messages())
