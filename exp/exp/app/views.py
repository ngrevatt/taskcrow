import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class CategoriesPage(APIView):
    def get(self, request):
        r = requests.get("http://models:8002/api/v1/category/")
        return Response({
            "categories": r.json()["records"]
        })

class CategoryTaskListPage(APIView):
    def get(self, request):
        payload = {"category": request.GET.get("category", -1)}
        r = requests.get("http://models:8002/api/v1/task/", params=payload)

        return Response({
            "tasks": r.json()["records"],
        })

class TaskDetailPage(APIView):
    def get(self, request):
        tid = request.GET.get("id", -1)
        r = requests.get("http://models:8002/api/v1/task/{}".format(tid))
        return Response({
            "task_detail": r.json(),
        })

