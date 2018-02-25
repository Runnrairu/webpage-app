from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('list',views.get_list),
    path('message',views.add_message),
    
]
