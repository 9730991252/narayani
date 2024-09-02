from django.urls import path
from owner import views
urlpatterns = [
    path('owner_dashboard/', views.owner_dashboard, name='owner_dashboard'),
    path('print_address/', views.print_address, name='print_address'),
]