# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_main_page, name='get_main_page'),
    # path('contact/', views.get_contact_page, name='get_contact_page'),
]
