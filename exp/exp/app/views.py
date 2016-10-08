import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class CategoriesPage(APIView):
    def get(self, request):
        r = requests.get("http://models/api/v1/category/")
        return Response({
            "categories": r.json()["records"]
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
        })

class TaskDetailPage(APIView):
    def get(self, request):
        tid = request.GET.get("task", -1)
        r = requests.get("http://models/api/v1/task/{}".format(tid))
        return Response({
            "task": r.json(),
        })

