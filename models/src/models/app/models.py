from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
    )

    phone_number = PhoneNumberField(blank=True)


class Customer(models.Model):
    user = models.OneToOneField(User, primary_key=True)


class ServiceProvider(models.Model):
    user = models.OneToToneField(User, primary_key=True)

    @property
    def is_verified(self):
        return self.verification.successful


class Verification
    service_provider = models.OneToOneField(ServiceProvider, primary_key=True)
    successful = models.BooleanField()
    failed = models.BooleanField()


class Category(models.Model):
    name = models.CharField(max_length=50)

class Task(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    category = models.ForeignKey(Category)
    description = models.TextField()
    cost = models.IntField()
    created_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeFIeld()
    complete = models.BooleanField(default=False)
    
