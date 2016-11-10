import json
import time
import requests
from elasticsearch import Elasticsearch
from kafka import KafkaConsumer
from kafka.common import NodeNotReadyError


def init_consumer():
    while True:
        try:
            consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
        except NodeNotReadyError:
            time.sleep(5)
        else:
            return consumer

consumer = init_consumer()

while True:
    try:
        r = requests.get("http://es:9200/")
    except:
        time.sleep(5)
    else:
        if r.status_code == 200:
            break

es = Elasticsearch(['es'])
if not es.indices.exists("listing_index"):
    es.indices.create(index='listing_index')

for message in consumer:
    listing = json.loads((message.value).decode('utf-8'))
    print(listing)
    es.index(index='listing_index', doc_type='listing', id=listing['id'], body=listing)

    es.indices.refresh(index="listing_index")
