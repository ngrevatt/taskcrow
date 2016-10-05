from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    username = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()

    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        return self.username


class Customer(models.Model):
    user = models.OneToOneField(UserProfile)

    def __str__(self):
        return str(self.user)


class ServiceProvider(models.Model):
    user = models.OneToOneField(UserProfile)

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
