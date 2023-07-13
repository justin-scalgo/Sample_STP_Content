from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_content, name='add_content'),
    path('edit/<int:pk>/', views.edit_content, name='edit_content'),
    path('delete/<int:pk>/', views.delete_content, name='delete_content'),
    path('', views.content_list, name='content_list'),
]
