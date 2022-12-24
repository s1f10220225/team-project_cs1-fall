from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('list', views.list, name='list'),
    path('test', views.test, name='test'),
]
