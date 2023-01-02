from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('list', views.list, name='list'),
    path('test', views.test, name='test'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/delete', views.delete, name='delete'),
    path('<int:article_id>/update', views.update, name='update'),
    path('<int:article_id>/like', views.like, name='like')
]
