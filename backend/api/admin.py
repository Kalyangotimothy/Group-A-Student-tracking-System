from django.contrib import admin
from .models import CustomUser,Department, Issue

admin.site.register(CustomUser)
admin.site.register(Department)
admin.site.register(Issue)
# Register your models here.

