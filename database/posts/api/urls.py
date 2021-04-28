from django.conf.urls import url
from django.urls import path, include
from .views import (
    MoviesListApiView,
    MoviesDetailApiView
)

urlpatterns = [
    path('', MoviesListApiView.as_view()),
    path('<int:movie_id>/', MoviesDetailApiView.as_view()),
]
