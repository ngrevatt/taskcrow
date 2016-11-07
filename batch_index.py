from elasticsearch import Elasticsearch
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('new-lsitings-topic', group='listing-indexer', bootstrap_servers='kafka:9092')
es = Elasticsearch(['es'])
if not es.indices.exists("listing_index"):
    es.indices.create(index='listing_index')

for message in consumer:
    listing = json.loads((message.value).decode('utf-8'))
    print(listing)
    es.index(index='listing_index', doc_type='listing', id=listing['id'], body=listing)

    es.indicies.refresh(index="listing_index")
