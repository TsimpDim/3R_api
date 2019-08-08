from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from api.models.Resource import Resource
from api.models.Option import Option

admin.site.register(Resource)
admin.site.register(Option)