from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('list', views.list, name='list'),
    path('test/<slug:genre>/<int:test_num>', views.test, name='test'),
    path('select', views.genre_select, name='genre_select'),
    path('select/<slug:genre>', views.num_select, name='num_select'),
    path('result/<slug:genre>/<int:test_num>', views.result, name='result'),
]
