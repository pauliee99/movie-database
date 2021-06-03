#from django.urls import include #path, include
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('api/', include('posts.api.urls')),
    url('docs/', views.documentation, name='docs'),
]
