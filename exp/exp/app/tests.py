import json
from django.test import TestCase
from kafka import KafkaProducer, KafkaConsumer

class ExperienceTestCase(TestCase):

    def test_task_create(self):
        some_new_listing = {
            "description": "Bleach the fence",
            "cost": 150,
            "created_date": "2016-09-15T17:02:00Z",
            "due_date": "2016-09-23T05:02:00Z",
            "complete": False,
            "customer": 1,
            "category": 1,
        }


        
        producer = KafkaProducer(bootstrap_servers='kafka:9092')
        producer.send('new-listing-topic', json.dumps(some_new_listing).encode('utf-8'))

        consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])

        for message in consumer:
            assertEquals(some_new_listing, json.loads((message.value).decode('utf-8')))


