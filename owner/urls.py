from django.urls import path
from owner import views
urlpatterns = [
    path('owner_dashboard/', views.owner_dashboard, name='owner_dashboard'),
]