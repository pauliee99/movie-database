from django.contrib import admin

# Register your models here.
from .models import movie, user, viewer, manager

class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Movie title and rating', {'fields': ['title', 'rating']}),
        ('Date information', {'fields': ['release_date']}),
    ]

admin.site.register(movie, MovieAdmin)

admin.site.register(viewer)
admin.site.register(manager)
