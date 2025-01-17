
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),  # Root URL for the store view
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
