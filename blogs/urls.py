from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='my_articles'),
    path('create/', views.article_create, name='article_create'),
    path('edit/<int:pk>/', views.article_edit, name='article_edit'),
    path('delete/<int:pk>/', views.article_delete, name='article_delete'),
]