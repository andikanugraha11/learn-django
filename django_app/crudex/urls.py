from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getAllPruduct, name='all_product'),
    path('add', views.addProduct, name='add_product'),
    path('update/<int:id>/', views.updateProduct, name='update_product'),
    path('delete/<int:id>/', views.deleteProduct, name='delete_product'),
    # path('details/<str:id>', views.details, name='details'),
]