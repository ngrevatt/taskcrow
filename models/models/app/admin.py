from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Customer)
admin.site.register(ServiceProvider)
admin.site.register(Verification)
admin.site.register(Category)
admin.site.register(Task)