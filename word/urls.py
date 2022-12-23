from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('test', views.test, name='test'),
]