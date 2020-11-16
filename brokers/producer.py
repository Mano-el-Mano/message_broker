import pika


class Producer:
    def __init__(self, config):
        self.config = config

    def create_connection(self):
        print(self.config)
        param = pika.ConnectionParameters(host=self.config['host'],
                                          port=self.config['port'])
        return pika.BlockingConnection(param)

    def basic_publish(self, routing_key: str, message):
        connection = self.create_connection()

        channel = connection.channel()

        channel.basic_publish(exchange=self.config['exchange'], routing_key=routing_key, body=message)
        print(f' Messaged published with {routing_key} with body {message}')

        connection.close()

    def fanout_publish(self, routing_key: str, message):
        connection = self.create_connection()

        channel = connection.channel()

        channel.exchange_declare(exchange=self.config['exchange'],
                                 exchange_type='fanout')

        channel.basic_publish(exchange=self.config['exchange'], routing_key=routing_key, body=message)
        print(f' Messaged published with {routing_key} with body {message}')

        connection.close()


