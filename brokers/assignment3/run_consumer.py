import json
from brokers.consumer import Consumer

with open('users.json') as users:
    parsed_users = json.load(users)
    config = {'host': 'localhost', 'port': 5672, 'exchange': 'loans', 'binding_key': 'loans'}

    consumer = Consumer('loans', '', config)
    consumer.setup_fanout()