import json
import logging

from kafka import KafkaConsumer
from kafka import KafkaProducer
from kafka.errors import KafkaError

from src.config import Settings
from src.infrastructure.parsers.parser_dispatcher import ParserDispatcher


class KafkaHandler:
    def __init__(self, settings: Settings = Settings):
        self._producer = KafkaProducer(
            bootstrap_servers=[settings.kafka.server],
            value_serializer=lambda x: json.dumps(x).encode("utf-8"),
        )
        self._consumer = KafkaConsumer(
            bootstrap_servers=[settings.kafka.server],
            group_id="1",
            auto_offset_reset="earliest",
        )
        self.__logger = logging.getLogger("KafkaLogger")

    @property
    def producer(self):
        return self._producer

    @property
    def consumer(self):
        return self._consumer

    async def send_message(self, topic: str, data: str):
        self.__logger.info(msg="Sending message to Kafka broker")

        try:
            message = self.producer.send(topic=topic, value=data)
            metadata = message.get()
            self.__logger.info(msg="Message has been sent to Kafka")
            return {"status": f"message has been sent to {metadata.topic} topic"}

        except KafkaError as e:
            self.__logger.error(msg=e.message)
            return {"error": e}

    async def get_message(self, topic):

        if self.consumer.subscription() is None:
            self.consumer.subscribe(topics=[topic])

        for message in self.consumer:
            self.__logger.info("Consumer got a message")
            url = json.loads(message.value)
            parser = ParserDispatcher().get_parser(url)
            if parser:
                await parser(url)
