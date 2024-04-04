from . import views
#from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('process_images/', views.process_images, name='process_images'),
    path('', views.render_index, name='render_index')
]