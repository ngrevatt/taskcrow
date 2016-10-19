import requests
from django.shortcuts import render_to_response
from .forms import LoginForm
from django.shortcuts import render
from django.http import HttpResponseRedirect


def categories_view(request):
    r = requests.get("http://exp/CategoriesPage")
    ctx = r.json()
    return render_to_response("app/categories.html", ctx)


def category_task_list_view(request, cid):
    payload = {
        "category": cid,
    }
    r = requests.get("http://exp/CategoryTaskListPage", params=payload)
    ctx = r.json()
    return render_to_response("app/category_task_list.html", ctx)


def task_detail_view(request, tid):
    payload = {
        "task": tid,
    }
    r = requests.get("http://exp/TaskDetailPage", params=payload)
    ctx = r.json()
    return render_to_response("app/task_detail.html", ctx)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = LoginForm()

    return render(request, 'app/login.html', {'form': form})



