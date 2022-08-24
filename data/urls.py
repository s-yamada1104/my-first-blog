from django.urls import path
from . import views
app_name = "data"
urlpatterns = [
    path('upload_sell/', views.upload_sell, name='upload_sell'),
    path('upload_member/', views.upload_member, name='upload_member'),
    path('upload_complete_sell/', views.upload_complete_sell, name='upload_complete_sell'),
    path('upload_complete_member/', views.upload_complete_member, name='upload_complete_member'),
]