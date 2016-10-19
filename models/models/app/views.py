from django.http import JsonResponse, HttpResponse
from django.core import exceptions
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, filters, views
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


class LoginView(views.APIView):
    def post(self, request):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == "" or password == "":
            return JsonResponse({
                "error": "must pass username and password"
            }, status=400)

        login_failure = JsonResponse({
            "error": "invalid username or password"
        })
        try:
            user = User.objects.get(username=username)
        except exceptions.ObjectDoesNotExist:
            return login_failure

        token = user.login(password)
        if token is None:
            return login_failure
        return JsonResponse({
            "token": token.token
        })


class LogoutView(views.APIView):
    def post(self, request):
        token = request.POST.get("token", "")
        if token == "":
            return JsonResponse({
                "error": "must pass token"
            }, status=400)

        AuthenticationToken.objects.filter(token=token).delete()

        return JsonResponse({
            "status": "OK"
        })


