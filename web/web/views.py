import requests
from django.shortcuts import render_to_response
from .forms import LoginForm
from .forms import UserForm
from .forms import ListingForm
from django.shortcuts import render
from django.http import HttpResponseRedirect




from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render # get_object_or_405
import urllib.request
import urllib.parse
import json
from django import template
from http import cookies
from django.core.urlresolvers import reverse, reverse_lazy, NoReverseMatch


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

def createuser(request):
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
            post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
            req = urllib.request.Request('http://exp/createuser', data=post_encoded, method='POST')
            resp_json = urllib.request.urlopen(req).read().decode('utf-8')
            resp = json.loads(resp_json)
            return render(request, 'home.html')

        else:
            print(account_form.errors)
    else:
        account_form = UserForm()

    return render(request, 'createUser.html', {'account_form': account_form})

def login(request):

    # auth = request.COOKIES.get('auth')
    # if  auth:
    #     return HttpResponseRedirect('/profile')
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print("cat")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            post_data = {'username': username, 'password': password}
            resp = requests.post('http://exp/login', data=post_data)
            print(resp)
            if resp.status_code != 200:
                return render(request, 'app/login.html')
            authenticator = {'auth': resp['authenticator'], 'user_id': resp['user_id']}
            response = HttpResponseRedirect('/profile')
            response.set_cookie("auth", json.dumps(authenticator))
            return response
        else:
            print(form)
    else:
        form = LoginForm()

    return render(request, 'app/login.html', {'form': form})


def log_out(request):
	auth = request.COOKIES.get('auth')
	jsona = json.loads(auth)
	post_data = {'u_id': jsona['user_id']}
	post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
	req = urllib.request.Request('http://exp/logout', data=post_encoded, method='POST')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	response = HttpResponseRedirect('app/logoutsuccess')
	response.set_cookie("auth", '', expires=-1)
	return response

def logoutsuccess(request):
	return render(request, 'app/logout.html')

def createListing(request):
	form = ListingForm()
	auth = request.COOKIES.get('auth')
	if not auth:
		return HttpResponseRedirect('/home')
	if request.method == 'POST':
		form = ListingForm(data=request.POST)
		if form.is_valid():
			title=form.cleaned_data['title']
			description=form.cleaned_data['description']
			jsona = json.loads(auth)
			post_data = {'title': title, 'description': description, 'creator': jsona['user_id'], 'available': True, 'u_id': jsona['user_id']}
			post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
			req = urllib.request.Request('http:/exp/createlisting', data=post_encoded, method='POST')
			expire_view_cache(request, 'home')
			resp_json = urllib.request.urlopen(req).read().decode('utf-8')
			resp = json.loads(resp_json)
			response = HttpResponseRedirect('app/create_listing_success/')
			return response
		else:
			print(form.errors)

	if request.method == 'GET':
    		return render(request, "app/createlistin.html", {'form': form})
    #f = ListingForm(request.POST)
	return render(request, "app/create_listing_success.html")

def createListingSuccess(request):
	return render(request, "app/create_listing_success.html")






