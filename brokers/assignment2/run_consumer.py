from brokers.consumer import Consumer


# here we could make a decorater function which always returns offers, and the routing_key,
# where we can both arguments using touple decoupling

def run():
    # We have made queue called advertising, where we can send offers
    # We then specify our routing key insider our generate_autumn_offers function
    # Where we send our offers through the queue
    config = {'host': 'localhost', 'port': 5672, 'exchange': 'loans', 'binding_key': 'loans'}

    consumer = Consumer('loans', '', config)
    consumer.setup_fanout()


if __name__ == '__main__':
    run()
