from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
    )

    phone_number =


class Customer(models.Model):
    user = models.OneToOneField(User, primary_key=True)

class ServiceProvider(models.Model):
    user = models.OneToToneField(User, primary_key=True)
    is_verified = models.BooleanField(default=False)

# Category (N)
# Task (N)
