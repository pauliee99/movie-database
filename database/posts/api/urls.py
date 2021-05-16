from django.urls import path, include
from .views import (
    MoviesListApiView,
    MoviesDetailApiView,
    EmailListApiView,
    EmailDetailApiView,
    UserListApiView,
    UserDetailApiView,
)

urlpatterns = [
    path('', MoviesListApiView.as_view()),
    path('<int:movie_id>/', MoviesDetailApiView.as_view()),
    path('mails/', EmailListApiView.as_view()),
    path('mails/<int:email_id>/', EmailDetailApiView.as_view()),
    path('users/', UserListApiView.as_view()),
    path('users/<int:user_id>', UserDetailApiView.as_view()),
    path('users/<str:username>', UserDetailApiView.as_view()),
]
