from django.contrib import admin
from .models import *
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Tag)