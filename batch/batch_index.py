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
        pass
    else:
        if r.status_code == 200:
            break
    time.sleep(5)

es = Elasticsearch(['es'])
es.indices.create(index='listing_index', ignore=400)


# Preload index
while True:
    try:
        r = requests.get("http://models/api/v1/task/")
    except Exception as e:
        pass
    else:
        if r.status_code == 200:
            break
    time.sleep(5)

for record in r.json()["records"]:
    es.index(index='listing_index', doc_type='listing', id=record["id"], body=record)
es.indices.refresh(index="listing_index")

# Digest queue
for message in consumer:
    listing = json.loads((message.value).decode('utf-8'))
    print(listing)
    es.index(index='listing_index', doc_type='listing', id=listing['id'], body=listing)
    es.indices.refresh(index="listing_index")
