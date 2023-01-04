from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('list', views.list, name='list'),
    path('test', views.test, name='test'),

	path('wordA', views.wordA, name='wordA'),
    path('<int:Word_id>/', views.detail, name='detail'),
    path('<int:Word_id>/delete', views.delete, name='delete'),
    path('<int:Word_id>/update', views.update, name='update'),
    path('<int:Word_id>/like', views.like, name='like')
]
