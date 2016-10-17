from rest_framework import viewsets, filters
from .serializers import *
from .models import *

class ListAsDictMixin(object):
    def list(self, request):
        resp = super().list(request)
        resp.data = {
            "records": resp.data,
        }
        return resp


class UserViewSet(ListAsDictMixin, viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerViewSet(ListAsDictMixin, viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ServiceProviderViewSet(ListAsDictMixin, viewsets.ModelViewSet):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer


class VerificationViewSet(ListAsDictMixin, viewsets.ModelViewSet):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerializer


class CategoryViewSet(ListAsDictMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TaskViewSet(ListAsDictMixin, viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_fields = ("id", "category",)

