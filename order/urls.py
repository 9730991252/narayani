from django.urls import path
from order import views
urlpatterns = [
    path('cart/', views.cart,name='cart'),
    path('order/', views.order,name='order'),
    path('pending_order/', views.pending_order,name='pending_order'),
    path('view_pending_order/<int:order_filter>', views.view_pending_order,name='view_pending_order'),
]