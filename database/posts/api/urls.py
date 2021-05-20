from django.urls import path, include
from .views import (
    MoviesListApiView,
    MoviesDetailApiView,
    EmailListApiView,
    EmailDetailApiView,
    UserListApiView,
    UserDetailApiView,
    ManagerListApiView,
    ManagerDetailApiView,
    ViewerListApiView,
    ViewerDetailApiView,
)

urlpatterns = [
    path('', MoviesListApiView.as_view()),
    path('<int:movie_id>/', MoviesDetailApiView.as_view()),
    path('mails/', EmailListApiView.as_view()),
    path('mails/<int:email_id>/', EmailDetailApiView.as_view()),
    path('users/', UserListApiView.as_view()),
    path('users/<int:user_id>', UserDetailApiView.as_view()),
    path('users/<str:username>', UserDetailApiView.as_view()),
    path('managers/', ManagerListApiView.as_view()),
    path('managers/<int:user_id>', ManagerDetailApiView.as_view()),
    path('viewers/', ViewerListApiView.as_view()),
    path('viewers/<int:user_id>', ViewerDetailApiView.as_view()),
]
