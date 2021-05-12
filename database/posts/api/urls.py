#from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import (
    MoviesListApiView,
    MoviesDetailApiView,
    #UserViewSet,
    #UsersListApiView,
    #UsersDetailApiView,
    EmailListApiView,
    EmailDetailApiView
)

#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)

urlpatterns = [
    path('', MoviesListApiView.as_view()),
    path('<int:movie_id>/', MoviesDetailApiView.as_view()),
    #path('users/', include(router.urls)),
    #path('users/', UsersListApiView.as_view()),
    #path('users/<int:user_id>/', UsersDetailApiView.as_view()),
    path('mails/', EmailListApiView.as_view()),
    path('mails/<int:email_id>/', EmailDetailApiView.as_view()),
]
