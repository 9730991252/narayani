from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('customer_logout/', views.customer_logout, name='customer_logout'),
]