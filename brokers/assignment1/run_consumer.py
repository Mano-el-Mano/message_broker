from brokers.consumer import Consumer


# here we could make a decorater function which always returns offers, and the routing_key,
# where we can both arguments using touple decoupling



def run():
    # We have made queue called advertising, where we can send offers
    # We then specify our routing key insider our generate_autumn_offers function
    # Where we send our offers through the queue
    config = {'host': 'localhost', 'port': 5672, 'exchange': 'advertising', 'binding_key': 'autumn_offers'}

    consumer = Consumer('advertising', 'autumn_offers', config)
    consumer.setup_topic()


if __name__ == '__main__':
    run()
