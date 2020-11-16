import pika
import json
from brokers.callback_handler import CallbackHandler


class Consumer:
    def __init__(self, queue_name, binding_key, config):
        self.queue_name = queue_name
        self.binding_key = binding_key
        self.config = config
        self.connection = self.create_connection()

    def create_connection(self):
        print(self.config)
        param = pika.ConnectionParameters(host=self.config['host'],
                                          port=self.config['port'])
        return pika.BlockingConnection(param)

    def on_message_callback(self, channel, method, properties, body):
        binding_key = method.routing_key
        print(f"received message for - + binding_key {binding_key}")
        parsed_body = json.loads(body)
        handler = CallbackHandler(['autumn_offers', 'loans'], {'filename': 'test.log'})
        handler.handle(binding_key, parsed_body)

    def setup_topic(self):
        channel = self.connection.channel()
        channel.exchange_declare(exchange=self.config['exchange'],
                                 exchange_type='topic')
        # This method creates or checks a queue
        channel.queue_declare(queue=self.queue_name, durable=True)
        # Binds the queue to the specified exchange
        channel.queue_bind(exchange=self.config['exchange'], queue=self.queue_name, routing_key=self.binding_key)
        channel.basic_consume(queue=self.queue_name,
                              on_message_callback=self.on_message_callback, auto_ack=True)
        print(f'waiting for data press CTRL + C to exit')
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()

    def setup_fanout(self):
        channel = self.connection.channel()
        channel.exchange_declare(exchange=self.config['exchange'],
                                 exchange_type='fanout')
        # This method creates or checks a queue
        result = channel.queue_declare(queue='', exclusive=True)

        queue_name = result.method.queue

        channel.queue_bind(exchange='loans', queue=queue_name)
        # Binds the queue to the specified exchange
        channel.basic_consume(queue=queue_name,
                              on_message_callback=self.on_message_callback, auto_ack=True)
        print("afte consume")
        print(f'waiting for data press CTRL + C to exit')
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
