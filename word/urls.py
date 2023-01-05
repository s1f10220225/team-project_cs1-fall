from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('list/<int:belong>', views.list, name='list'),
    path('list/select', views.genre_list, name='genre_list'),
    path('list/select/<int:genre>', views.name_list, name='name_list'),
    path('test/<int:belong>', views.test, name='test'),
    path('test/select', views.genre_select, name='genre_select'),
    path('test/select/<int:genre>', views.num_select, name='num_select'),
    path('test/result/<int:belong>', views.result, name='result'),
]
