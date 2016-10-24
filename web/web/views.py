import requests
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from .forms import UserForm
from .forms import ListingForm


def add_auth_header(exp_request, web_request):
    exp_request.headers["auth"] = web_request.COOKIES.get("auth", "")

def categories_view(request):
    r = requests.get("http://exp/CategoriesPage")
    add_auth_header(r, request)
    ctx = r.json()
    return render(request, "app/categories.html", ctx)


def category_task_list_view(request, cid):
    payload = {
        "category": cid,
    }
    r = requests.get("http://exp/CategoryTaskListPage", params=payload)
    add_auth_header(r, request)
    ctx = r.json()
    return render(request, "app/category_task_list.html", ctx)


def task_detail_view(request, tid):
    payload = {
        "task": tid,
    }
    r = requests.get("http://exp/TaskDetailPage", params=payload)
    add_auth_header(r, request)
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
            phone_number = account_form.cleaned_data['phone_number']
            post_data = {'username': username, 'password': password, 'first_name': first_name, 'last_name': last_name,
                         'email': email, 'phone_number': phone_number}
            resp = requests.post('http://exp/SignUpPage/', data = post_data)
            if resp.status_code != 200:
                return render(request, 'app/createuser.html')
            data = resp.json()
            if "error" in data:
                return render(request, 'app/createuser.html')
            response = redirect("main_view")
            return response
        else:
            print(account_form)
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
            resp = requests.post("http://exp/LoginPage/", data=post_data)
            if resp.status_code != 200:
                return render(request, "app/login.html", {"form": form})
            data = resp.json()
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

    return render(request, "app/login.html", {"form": form})


def logout_view(request):
    token = request.COOKIES.get("auth", "")
    payload = {
        "token": token
    }
    r = requests.post("http://exp/LogoutPage/", data=payload)
    if r.status_code != 200:
        return HttpResponse("Error logging out", status=500)

    response = redirect("main_view")
    response.set_cookie("auth", "", expires=-1)
    return response


def createListing(request):
    pass
    auth = request.COOKIES.get("auth")
    if not auth:
        return HttpResponseRedirect('/')
    if request.method == 'GET':
        return render(request, 'app/createlistin.html')
    if request.method == 'POST':
        form = ListingForm(data=request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            jsona = json.loads(auth)
            post_data = {'category': category, 'description': description, 'creator': jsona['user_id'],
                         'available': True}
            resp = requests.post('http:/exp/CreateTaskPage/', data=post_data)
            if resp.status_code != 200:
                return render(request, 'app/createlistin.html')
            data = resp.json()
            if "error" in data:
                return render(request, 'app/createlistin.html')
            authenticator = data["token"]
            response = HttpResponseRedirect('/')
            return response
        else:
            print(form)
    else:
        form = ListingForm()

    return render(request, 'app/createlistin.html', {'form': form})


