from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_packages, name='get_packages'),
]
