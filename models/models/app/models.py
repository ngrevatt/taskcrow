import os
import hmac
from django.conf import settings
from django.core import exceptions
from django.db import models
from django.utils import timezone
from django.contrib.auth import hashers
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()

    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        return self.username

    def login(self, password):
        token = None
        if hashers.check_password(password, self.password):
            token = AuthenticationToken.create_for_user(self)
        return token

    def logout(self, token):
        try:
            at = AuthenticationToken.get(user=self, token=tokeon)
            at.delete()
            return True
        except exceptions.ObjectDoesNotExist:
            return False


class AuthenticationToken(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length=64, primary_key=True)
    created_date = models.DateTimeField(default=timezone.now)

    @classmethod
    def create_for_user(cls, user):
        token = hmac.new(key = settings.SECRET_KEY.encode("utf-8"),
                         msg = os.urandom(32), digestmod = "sha256").hexdigest()
        return AuthenticationToken.objects.create(user=user, token=token)


class Customer(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return str(self.user)


class ServiceProvider(models.Model):
    user = models.OneToOneField(User)

    @property
    def is_verified(self):
        return self.verification.successful

    def __str__(self):
        return str(self.user)


class Verification(models.Model):
    service_provider = models.OneToOneField(ServiceProvider)
    complete = models.BooleanField()
    successful = models.BooleanField()

    def __str__(self):
        return str(self.service_provider)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

    class Meta(object):
        verbose_name_plural = "categories"


class Task(models.Model):
    customer = models.ForeignKey(Customer)
    category = models.ForeignKey(Category)
    description = models.TextField()
    cost = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.customer)

