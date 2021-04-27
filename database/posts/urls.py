from django.urls import path, include
from django.conf.urls import url

#from . import views

urlpatterns = [
    path('api/', include('posts.api.urls')),
]
