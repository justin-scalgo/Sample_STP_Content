from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.add_content, name='add_content'),
    path('edit/', views.edit_content, name='edit_content'),
    path('delete/', views.delete_content, name='delete_content'),
    path('', views.content_list, name='content_list'),
    path('cms-content/<int:pk>/', views.fetch_cms_content, name='fetch_cms_content'),
]
