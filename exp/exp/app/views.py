import requests
import json
from elasticsearch import Elasticsearch
from kafka import KafkaProducer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

def get_authenticated_user(request):
    token = request.META.get("HTTP_AUTH", "")
    ru = requests.get("http://models/api/v1/authenticated_user/",
            headers={"auth": token})
    j = ru.json()
    if "error" in j:
        return None
    else:
        return j.get("user", None)


def auth_headers(request):
    return {
        "auth": request.META.get("HTTP_AUTH", ""),
    }

class CategoriesPage(APIView):
    def get(self, request):
        rc = requests.get("http://models/api/v1/category/")
        return Response({
            "categories": rc.json()["records"],
            "user": get_authenticated_user(request),
        })

class CategoryTaskListPage(APIView):
    def get(self, request):
        cid = request.GET.get("category", -1)
        payload = {"category": cid}
        tr = requests.get("http://models/api/v1/task/", params=payload)

        cr = requests.get("http://models/api/v1/category/{}".format(cid))

        return Response({
            "category": cr.json(),
            "tasks": tr.json()["records"],
            "user": get_authenticated_user(request),
        })

class TaskDetailPage(APIView):
    def get(self, request):
        tid = request.GET.get("task", -1)
        r = requests.get("http://models/api/v1/task/{}".format(tid))
        task = dict(r.json())

        customer_id = task["customer"]
        customer = requests.get("http://models/api/v1/user/{}".format(customer_id)).json()
        task["customer"] = customer

        category_id = task["category"]
        category = requests.get("http://models/api/v1/category/{}".format(category_id)).json()
        task["category"] = category

        return Response({
            "task": task,
            "user": get_authenticated_user(request),
        })

class SignUpPage(APIView):
    def post(self, request):
        sr = requests.post("http://models/api/v1/signup/", data=request.POST)
        return Response(sr.json(), status=sr.status_code)


class CreateTaskPage(APIView):
    def get(self, request):
        r = requests.get("http://models/api/v1/category/")
        return Response({
            "user": get_authenticated_user(request),
            "categories": r.json()["records"],
        })

    def post(self, request):
        user = get_authenticated_user(request)
        payload = {
            "customer": user["id"],
            "due_date": request.POST.get("due_date", ""),
            "description": request.POST.get("description", ""),
            "cost": request.POST.get("cost", ""),
            "category": request.POST.get("category", ""),
        }


        r = requests.post("http://models/api/v1/task/", data=payload, headers=auth_headers(request))

        producer = KafkaProducer(bootstrap_servers="kafka:9092")
        producer.send("new-listings-topic", r.text.encode("utf-8"))

        return Response({
            "task": r.json(),
            "user": user,
        },  status=r.status_code)


class LoginPage(APIView):
    def get(self, request):
        return Response({
            "user": get_authenticated_user(request),
        })

    def post(self, request):
        user = request.POST.get("username", "")
        password = request.POST.get("password", "")
        payload = {"username": user, "password": password}

        ar = requests.post("http://models/api/v1/login/", data=payload)

        return Response(ar.json(), status=ar.status_code)


class LogoutPage(APIView):
    def post(self, request):
        token = request.POST.get("token", "")
        payload = {"token": token}

        lr = requests.post("http://models/api/v1/logout/", data=payload)

        return Response(lr.json(), status=lr.status_code)


class SearchPage(APIView):
    def get(self, request):
        query = request.GET.get("query", "")

        es = Elasticsearch(["es"])

        body = {
            "query": {
                "query_string": {
                    "query": query,
                }
            },
            "size": 20,
        }
        results = es.search(index="listing_index", body=body)

        return Response({
            "results": [h["_source"] for h in results["hits"]["hits"]],
        })
