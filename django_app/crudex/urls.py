from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getAllPruduct, name='index'),
    # path('details/<str:id>', views.details, name='details'),
]