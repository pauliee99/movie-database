from django.contrib import admin

# Register your models here.
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Movie title and rating', {'fields': ['title', 'rating']}),
        ('Date information', {'fields': ['release_date']}),
    ]

admin.site.register(Movie, MovieAdmin)
