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

    def test_category_list(self):
        got = self.client.get("/api/v1/category/").data
        want = {
            "records": [
                {
                    "id": 1,
                    "name": "Yard Work"
                },
                {
                    "id": 2,
                    "name": "Cleaning"
                }
            ]
        }
        self.assertEquals(got, want)

    def test_category_detail(self):
        got = self.client.get("/api/v1/category/1/").data
        want = {
            "id": 1,
            "name": "Yard Work",
        }
        self.assertEquals(got, want)

    def test_task_list(self):
        got = self.client.get("/api/v1/task/").data
        want = {
            "records": [
                {
                    "id": 1,
                    "description": "Rake leaves",
                    "cost": 100,
                    "created_date": "2016-09-15T17:02:00Z",
                    "due_date": "2016-09-23T05:02:00Z",
                    "complete": False,
                    "customer": {
                        "id": 1,
                        "user": {
                            "id": 1,
                            "username": "bob",
                            "first_name": "Bob",
                            "last_name": "Jones",
                            "email": "bob@email.com",
                            "phone_number": "+41524204242"
                        }
                    },
                    "category": {
                        "id": 1,
                        "name": "Yard Work"
                    }
                },
                {
                    "id": 2,
                    "description": "Powerwash house",
                    "cost": 100,
                    "created_date": "2016-09-15T17:02:00Z",
                    "due_date": "2016-09-23T05:02:00Z",
                    "complete": False,
                    "customer": {
                        "id": 1,
                        "user": {
                            "id": 1,
                            "username": "bob",
                            "first_name": "Bob",
                            "last_name": "Jones",
                            "email": "bob@email.com",
                            "phone_number": "+41524204242"
                        }
                    },
                    "category": {
                        "id": 2,
                        "name": "Cleaning"
                    }
                }
            ]
        }
        self.assertEquals(got, want)

    def test_task_detail(self):
        got = self.client.get("/api/v1/task/1/").data
        want = {
            "id": 1,
            "description": "Rake leaves",
            "cost": 100,
            "created_date": "2016-09-15T17:02:00Z",
            "due_date": "2016-09-23T05:02:00Z",
            "complete": False,
            "customer": {
                "id": 1,
                "user": {
                    "id": 1,
                    "username": "bob",
                    "first_name": "Bob",
                    "last_name": "Jones",
                    "email": "bob@email.com",
                    "phone_number": "+41524204242"
                }
            },
            "category": {
                "id": 1,
                "name": "Yard Work"
            }
        }
        self.assertEquals(got, want)

    def test_customer_list(self):
        got = self.client.get("/api/v1/customer/").data
        want = {
            "records": [
                {
                    "id": 1,
                    "user": 1
                },
                {
                    "id": 2,
                    "user": 2
                },
            ]
        }
        self.assertEqual(got, want)

    def test_customer_detail(self):
        got = self.client.get("/api/v1/customer/1/").data
        want = {
            "id": 1,
            "user": 1
        }
        self.assertEquals(got, want)

    def test_service_provider_list(self):
        got = self.client.get("/api/v1/service_provider/").data
        want = {
            "records": [
                {
                    "id": 1,
                    "user": 2
                },
            ]
        }
        self.assertEqual(got, want)

    def test_service_provider_detail(self):
        got = self.client.get("/api/v1/service_provider/1/").data
        want = {
            "id": 1,
            "user": 2
        }
        self.assertEqual(got, want)

    def test_verification_list(self):
        got = self.client.get("/api/v1/verification/").data
        want = {
            "records": [
                {
                    "id": 1,
                    "complete": True,
                    "successful": True,
                    "service_provider": 1
                },
            ]
        }
        self.assertEqual(got, want)

    def test_verification_detail(self):
        got = self.client.get("/api/v1/verification/1/").data
        want = {
            "id": 1,
            "complete": True,
            "successful": True,
            "service_provider": 1
        }
        self.assertEqual(got, want)
