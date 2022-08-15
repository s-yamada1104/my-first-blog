from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('blog/upload/', views.upload, name='upload'),
    path('blog/upload_complete/', views.upload_complete, name='upload_complete'),
]