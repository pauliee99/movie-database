from django.contrib import admin

# Register your models here.
from .models import movies, users

admin.site.register(movies)
admin.site.register(users)