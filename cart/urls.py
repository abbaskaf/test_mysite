from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartView, name='Cart'),
    path('', views.AddCart, name='AddCart')
]
