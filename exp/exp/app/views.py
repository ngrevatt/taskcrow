import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class CategoriesPage(APIView):
    def get(self, request):
        r = requests.get("http://models:8002/api/v1/category/")
        return Response(r.json())
