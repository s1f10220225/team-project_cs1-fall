from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('list/<int:belong>', views.list, name='list'),
    path('list/select', views.genre_list, name='genre_list'),
    path('list/select/<int:genre>', views.name_list, name='name_list'),
    path('word/edit/<int:word_num>/<int:belong>', views.word_edit, name='word_edit'),
    path('word/add/<int:belong>', views.word_add, name='word_add'),
    path('word/update/<int:belong>/<int:select>', views.word_update, name='word_update'),
    path('word/delete/<int:word_num>/<int:belong>', views.word_delete, name='word_delete'),
    path('test/select', views.genre_select, name='genre_select'),
    path('test/select/<int:genre>', views.num_select, name='num_select'),
    path('test/result/<int:belong>', views.result, name='result'),
]
