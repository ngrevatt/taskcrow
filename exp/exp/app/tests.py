from django.test import TestCase

class ExperienceTestCase(TestCase):

    def test_task_create(self):
        payload = {
            "description": "Bleach the fence",
            "cost": 150,
            "created_date": "2016-09-15T17:02:00Z",
            "due_date": "2016-09-23T05:02:00Z",
            "complete": False,
            "customer": 1,
            "category": 1,
        }
        
