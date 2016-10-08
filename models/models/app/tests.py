from django.test import TestCase, Client
from .models import *

class ModelsTestCase(TestCase):
    fixtures = ["fixtures.json"]

    def test_user_profile_list(self):
        got = self.client.get("/api/v1/user_profile/").data
        want = {
            "records": [
                {
                    "id": 1,
                    "username": "bob",
                    "first_name": "Bob",
                    "last_name": "Jones",
                    "email": "bob@email.com",
                    "phone_number": "+41524204242"
                },
                {
                    "id": 2,
                    "username": "mary",
                    "first_name": "Mary",
                    "last_name": "Jones",
                    "email": "mary@email.com",
                    "phone_number": "+41524204241"
                }
            ]
        }
        self.assertEquals(got, want)

    def test_user_profile_detail(self):
        got = self.client.get("/api/v1/user_profile/1/").data
        want = {
	    "id": 1,
	    "username": "bob",
	    "first_name": "Bob",
	    "last_name": "Jones",
	    "email": "bob@email.com",
	    "phone_number": "+41524204242"
	}
        self.assertEquals(got, want)
