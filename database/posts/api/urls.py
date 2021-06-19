from django.conf.urls import include
from django.urls import path
from .views import (
    MoviesListApiView,
    MoviesDetailApiView,
    EmailListApiView,
    EmailDetailApiView,
)

urlpatterns = [
    path('', MoviesListApiView.as_view()),
    path('<int:movie_id>/', MoviesDetailApiView.as_view()),
    path('mails/', EmailListApiView.as_view()),
    path('mails/<int:email_id>/', EmailDetailApiView.as_view()),
]
