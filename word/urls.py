from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('list/<int:genre>/<int:test_num>', views.list, name='list'),
    path('list/select', views.genre_list, name='genre_list'),
    path('list/select/<int:genre>', views.name_list, name='name_list'),
    path('test/<slug:genre>/<int:test_num>', views.test, name='test'),
    path('test/select', views.genre_select, name='genre_select'),
    path('test/select/<slug:genre>', views.num_select, name='num_select'),
    path('test/result/<slug:genre>/<int:test_num>', views.result, name='result'),
]
