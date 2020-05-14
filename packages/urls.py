from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_packages, name='get_packages'),
    path('update_cart/<package_id>', views.update_cart, name='update_cart')
]
