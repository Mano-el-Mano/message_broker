from brokers.producer import Producer
from brokers.consumer import Consumer
import json

def generate_autumn_offers():
    routing_key = "autumn_offers"
    offers = [{'name': 'Gucci Tshirt', 'discount': 200},
              {'name': 'Prada Bag', 'discount': 300},
              {'name': 'Billa Bong Tanktop', 'discount': 150}]
    return offers, routing_key

def run_app():
    producer_config = {'host': 'localhost', 'port': 5672, 'exchange': 'advertising'}
    producer = Producer(producer_config)
    offers, routing_key = generate_autumn_offers()
    print(routing_key)
    for elem in offers:
        print(producer.basic_publish("autumn_offers", json.dumps(elem)))



if '__main__' == __name__:
    run_app()