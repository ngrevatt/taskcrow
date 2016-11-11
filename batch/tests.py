import unittest
import json
from batch_index import BatchJob


class MockQueueMessage(object):
    def __init__(self, d):
        self.value = json.dumps(d).encode("utf-8")


class MockConsumer(object):
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.items):
            return MockQueueMessage(self.items.pop(0))
        else:
            raise StopIteration


class MockElasticSearchIndices(object):
    def create(self, **kwargs):
        pass

    def refresh(self, **kwargs):
        pass

class MockElasticSearch(object):
    def __init__(self):
        self.indices = MockElasticSearchIndices()
        self.search_indices = {}

    def index(self, index="", doc_type="", id=0, body={}):
        if index not in self.search_indices:
            self.search_indices[index] = {}
        self.search_indices[index][id] = body


class BatchTests(unittest.TestCase):
    def setUp(self):
        self.items = [
            {
                "id": 0,
                "description": "Bleach the fence",
                "cost": 150,
                "created_date": "2016-09-15T17:02:00Z",
                "due_date": "2016-09-23T05:02:00Z",
                "complete": False,
                "customer": 1,
                "category": 1,
            },
            {
                "id": 1,
                "description": "Un-bleach the fence",
                "cost": 1500,
                "created_date": "2016-09-15T17:02:00Z",
                "due_date": "2016-09-23T05:02:00Z",
                "complete": False,
                "customer": 1,
                "category": 1,
            },
        ]
        mock_consumer = MockConsumer(self.items)
        self.mock_es = MockElasticSearch()
        self.b = BatchJob(mock_consumer, self.mock_es)

    def test_batch(self):
        self.b.init()
        self.b.run()
        for item in self.items:
            self.assertDictEqual(
                item,
                self.mock_es.search_indices["listing_index"][item["id"]]
            )
