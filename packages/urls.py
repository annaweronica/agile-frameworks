from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_packages, name='get_packages'),
    path('update_cart/<package_id>', views.update_cart, name='update_cart'),
    path('package_management/', views.get_package_management, name='get_package_management'),
    path('add/', views.add_package, name='add_package'),
    path('edit/<package_id>/', views.edit_package, name='edit_package'),
    path('delete/<package_id>/', views.delete_package, name='delete_package'),
]
