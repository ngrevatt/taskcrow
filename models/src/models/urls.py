"""models URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers
from .app import views


router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'user_profile', views.UserProfileViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'service_provider', views.ServiceProviderViewSet)
router.register(r'verification', views.VerificationViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'task', views.TaskViewSet)

admin.autodiscover()

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
