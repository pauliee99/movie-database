from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('api/', include('posts.api.urls')),
]
