from django.urls import path
from ajax import views
urlpatterns = [
    path('save_category', views.save_category, name='save_category'),
    path('search_product', views.search_product, name='search_product'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('state', views.state, name='state'),
    path('in_stock', views.in_stock, name='in_stock'),
    path('cart_qty', views.cart_qty, name='cart_qty'),
    path('check_customer_mobile', views.check_customer_mobile, name='check_customer_mobile'),
]