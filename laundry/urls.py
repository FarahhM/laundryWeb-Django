from django.urls import path
from .views import (UserCreateAPIView, UserLoginAPIView, ClassificationAPIView, ItemListView, ItemCreatView, AddToCartView, 
ItemUpdateView, RemoveFromCartView, OrderSummaryView, CheckoutView)

urlpatterns= [
path('login/', UserLoginAPIView.as_view(), name='login'),
path('signup/', UserCreateAPIView.as_view(), name='signup'),
path('classification/', ClassificationAPIView.as_view(), name='classification'),
path('item-list/', ItemListView.as_view(), name='item-list'),
path('item-create/', ItemCreatView.as_view(), name='item-create') ,
path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
path('update/<int:item_id>/', ItemUpdateView.as_view(), name='item-update'),
path('remove-from-cart/', RemoveFromCartView.as_view(), name='remove-from-cart'),
path('orders/', OrderSummaryView.as_view(), name='orders'),
path('checkout/', CheckoutView.as_view(), name='checkout')
]
