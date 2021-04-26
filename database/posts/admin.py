from django.contrib import admin

# Register your models here.
from .models import movie, user, viewer, manager

admin.site.register(movie)
admin.site.register(user)
admin.site.register(viewer)
admin.site.register(manager)
