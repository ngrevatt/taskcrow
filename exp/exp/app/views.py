import requests
import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class CategoriesPage(APIView):
    def get(self, request):
        token = request.headers.get("auth", "")
        ru = None

        rc = requests.get("http://models/api/v1/category/")
        return Response({
            "categories": rc.json()["records"],
            "user": ru.json(),
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

class SignUpPage(APIView):
    def post(self, request):
        sr = requests.post("http://models/api/v1/user/", data=request.POST)
        return Response(sr.json(), status=sr.status_code)


class CreateTaskPage(APIView):
    def post(self, request):
        r = requests.post("http://models/api/v1/task/", data=request.POST)
        return Response(r.json(), status=r.status_code)


class LoginPage(APIView):
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


