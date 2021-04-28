from django.conf.urls import url
from django.urls import path, include
from .views import (
    MoviesListApiView,
)

urlpatterns = [
    path('', MoviesListApiView.as_view()),
]
