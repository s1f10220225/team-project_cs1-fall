from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('first/list_select', views.first_genre_select),
    path('first/list_select/<int:genre>', views.first_list_select),
    path('list/<int:belong>', views.list, name='list'),
    path('cd_genre', views.cd_genre, name='cd_genre'),
    path('create_genre', views.create_genre, name='create_genre'),
    path('delete_genre/<int:genre>', views.genre_delete, name='genre_delete'),
    path('cd_list/<int:genre>', views.cd_list, name='cd_list'),
    path('create_list/<int:genre>', views.create_list, name='create_list'),
    path('delete_list/<int:genre>/<int:id>', views.list_delete, name='list_delete'),
    path('list/select', views.genre_list, name='genre_list'),
    path('list/select/<int:genre>', views.name_list, name='name_list'),
    path('word/edit/<int:word_num>/<int:belong>', views.word_edit, name='word_edit'),
    path('word/add/<int:belong>', views.word_add, name='word_add'),
    path('word/update/<int:belong>/<int:select>', views.word_update, name='word_update'),
    path('word/delete/<int:word_num>/<int:belong>', views.word_delete, name='word_delete'),
    path('test/select', views.genre_select, name='genre_select'),
    path('test/select/<int:genre>', views.num_select, name='num_select'),
    path('test/<int:belong>', views.test, name='test'),
    path('test/<int:belong>/error', views.test_error, name='test_error'),
    path('test/result/<int:belong>', views.result, name='result'),
]
