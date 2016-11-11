import requests
import json
from json.decoder import JSONDecodeError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from .forms import UserForm
from .forms import ListingForm


def auth_headers(request):
    return {
        "auth": request.COOKIES.get("auth", ""),
    }

def request_successful(response):
    return 200 <= response.status_code < 300


def categories_view(request):
    r = requests.get("http://exp/api/v1/CategoriesPage/",
            headers=auth_headers(request))
    ctx = r.json()
    return render(request, "app/categories.html", ctx)


def category_task_list_view(request, cid):
    payload = {
        "category": cid,
    }
    r = requests.get("http://exp/api/v1/CategoryTaskListPage/", params=payload,
            headers=auth_headers(request))
    ctx = r.json()
    return render(request, "app/category_task_list.html", ctx)


def task_detail_view(request, tid):
    payload = {
        "task": tid,
    }
    r = requests.get("http://exp/api/v1/TaskDetailPage/", params=payload,
            headers=auth_headers(request))
    ctx = r.json()
    return render(request, "app/task_detail.html", ctx)


def signup_view(request):
    if request.method == 'POST':
        account_form = UserForm(request.POST)
        if account_form.is_valid():
            first_name = account_form.cleaned_data['first_name']
            last_name = account_form.cleaned_data['last_name']
            username = account_form.cleaned_data['username']
            password = account_form.cleaned_data['password']
            email = account_form.cleaned_data['email']
            phone_number = account_form.cleaned_data['phone_number'].as_international
            post_data = {'username': username, 'password': password, 'first_name': first_name, 'last_name': last_name,
                         'email': email, 'phone_number': phone_number}
            resp = requests.post('http://exp/api/v1/SignUpPage/', data=post_data)

            try:
                data = resp.json()
                error = data.get("error", "")
            except JSONDecodeError:
                error = "An unknown error occurred"

            if not request_successful(resp):
                return render(request, 'app/createuser.html', {"account_form": account_form, "error": error})

            data = resp.json()
            if "error" in data:
                ctx = {
                    "account_form": account_form,
                    "error": error,
                }
                return render(request, 'app/createuser.html', ctx)
            response = redirect("login_view")
            return response
    else:
        account_form = UserForm()

    return render(request, 'app/createuser.html', {'account_form': account_form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            post_data = {"username": username, "password": password}

            r = requests.post("http://exp/api/v1/LoginPage/", data=post_data,
                    headers=auth_headers(request))

            if not request_successful(r):
                return render(request, "app/login.html", {"form": form})

            data = r.json()
            if "error" in data:
                ctx = {
                    "form": form,
                    "error": data["error"]
                }
                return render(request, "app/login.html", ctx)

            authenticator = data["token"]
            response = redirect("main_view")
            response.set_cookie("auth", authenticator)
            return response
    else:
        form = LoginForm()


    r = requests.get("http://exp/api/v1/LoginPage/", headers=auth_headers(request))

    ctx = {
            "form": form,
            "user": r.json().get("user", None),
    }

    return render(request, "app/login.html", {"form": form})


def logout_view(request):
    token = request.COOKIES.get("auth", "")
    payload = {
        "token": token
    }
    r = requests.post("http://exp/api/v1/LogoutPage/", data=payload)
    if not request_successful(r):
        return redirect("main_view")

    response = redirect("main_view")
    response.set_cookie("auth", "", expires=-1)
    return response


def create_listing_view(request):
    auth = request.COOKIES.get("auth")
    if not auth:
        return redirect("login_view")
    if request.method == 'POST':
        form = ListingForm(data=request.POST)
        if form.is_valid():
            resp = requests.post('http://exp/api/v1/CreateTaskPage/', data=form.cleaned_data,
                    headers=auth_headers(request))
            if not request_successful(resp):
                return render(request, 'app/createlisting.html',
                        {"form": form, "error": "There was an error creating this task: {}".format(resp.text)})

            data = resp.json()
            if "error" in data:
                return render(request, 'app/createlisting.html', {"form": form, "error": error})
            return redirect("task_detail_view", data["task"]["id"])
    else:
        form = ListingForm()

    r = requests.get("http://exp/api/v1/CreateTaskPage/", headers=auth_headers(request))

    data = r.json()
    user = data.get("user", None)
    if not user:
        return redirect("login_view")

    ctx = {
            "form": form,
            "user": user,
            "categories": data["categories"]
    }

    return render(request, 'app/createlisting.html', ctx)

def search_view(request):
    query = request.GET.get("query", "")

    payload = {
        "query": query
    }
    r = requests.get("http://exp/api/v1/SearchPage/", params=payload)

    results = r.json()["results"]
    ctx = {
        "query": query,
        "search_results": results,
    }
    return render(request, "app/search.html", ctx)

