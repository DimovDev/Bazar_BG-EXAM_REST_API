from django.contrib import admin

# Register your models here.
from django.contrib import admin

# from __future__ import unicode_literals

from django.contrib import admin
from .models import UserProfile, StatusUpdate, Message

admin.site.register(UserProfile)
admin.site.register(StatusUpdate)
admin.site.register(Message)
