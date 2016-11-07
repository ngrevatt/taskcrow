"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r"^$", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r"^$", Home.as_view(), name="home")
Including another URLconf
    1. Add a URL to urlpatterns:  url(r"^blog/", include("blog.urls"))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r"^$", views.categories_view, name="main_view"),
    url(r"^category/(?P<cid>\d+)$", views.category_task_list_view,
        name="category_task_list_view"),
    url(r"^task/(?P<tid>\d+)/$", views.task_detail_view,
        name="task_detail_view"),
    url(r"^login/$", views.login_view, name="login_view"),
    url(r"^logout/$", views.logout_view, name="logout_view"),
    url(r"^signup/$", views.signup_view, name="signup_view"),
    url(r"^create_listing/$", views.create_listing_view,
        name="create_listing_view"),
    url(r"^search/$", views.search_view,
        name="search_view"),
]
