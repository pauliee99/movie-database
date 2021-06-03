from django.conf.urls import url, include
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
    url('', MoviesListApiView.as_view()),
    url('<int:movie_id>/', MoviesDetailApiView.as_view()),
    url('mails/', EmailListApiView.as_view()),
    url('mails/<int:email_id>/', EmailDetailApiView.as_view()),
    url('users/', UserListApiView.as_view()),
    url('users/<int:user_id>', UserDetailApiView.as_view()),
    url('users/<str:username>', UserDetailApiView.as_view()),
    url('managers/', ManagerListApiView.as_view()),
    url('managers/<int:user_id>', ManagerDetailApiView.as_view()),
    url('viewers/', ViewerListApiView.as_view()),
    url('viewers/<int:user_id>', ViewerDetailApiView.as_view()),
]
