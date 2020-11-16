from brokers.producer import Producer
from brokers.consumer import Consumer
import uuid
import json

def generate_loan_request():
    offers = [{'id': str(uuid.uuid4()), 'price': 5000},
              {'id': str(uuid.uuid4()), 'price': 7000},
              {'id': str(uuid.uuid4()), 'price': 8000}]
    return offers

def run_app():
    producer_config = {'host': 'localhost', 'port': 5672, 'exchange': 'loans'}
    producer = Producer(producer_config)
    offers = generate_loan_request()
    for elem in offers:
        print(producer.fanout_publish("loans", json.dumps(elem)))



if '__main__' == __name__:
    run_app()