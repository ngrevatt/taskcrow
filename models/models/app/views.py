from django.http import JsonResponse, HttpResponse
from django.core import exceptions
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, filters, views
from rest_framework.permissions import IsAuthenticatedOrReadOnly
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
    #permission_classes = (IsAuthenticatedOrReadOnly,)


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

class SignupView(views.APIView):
    def post(self, request):
        p = request.POST
        User.objects.create(
            username=p["username"],
            password=hashers.make_password(p["password"]),
            first_name=p["first_name"],
            last_name=p["last_name"],
            email=p["email"],
            phone_number=p["phone_number"],
        )

        return JsonResponse({
            "status": "CREATED"
        }, status=201)


class AuthenticatedUserView(views.APIView):
    def get(self, request):
        token = request.META.get("HTTP_AUTH", "")
        if token == "":
            return JsonResponse({
                "error": "no token provided",
            }, status=400)

        try:
            auth_token = AuthenticationToken.objects.get(token=token)
        except exceptions.ObjectDoesNotExist:
            return JsonResponse({
                "error": "no user for given authentication token"
            }, status=404)

        return JsonResponse({
            "user": UserSerializer(auth_token.user).data,
        })
