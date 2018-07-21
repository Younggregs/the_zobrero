# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Account, Category, Talent, Chat
from django.contrib import admin

# Register your models here.

admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Talent)
admin.site.register(Chat)
