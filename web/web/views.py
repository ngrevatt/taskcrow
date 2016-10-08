import requests
from django.shortcuts import render_to_response


def categories_view(request):
    r = requests.get("http://exp/CategoriesPage")
    ctx = r.json()
    return render_to_response("app/categories.html", ctx)


def category_task_list_view(request, cid):
    payload = {
        "id": cid,
    }
    r = requests.get("http://exp/CategoryTaskListPage", params=payload)
    ctx = r.json()
    return render_to_response("app/category_task_list.html", ctx)

