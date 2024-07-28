from django.urls import path
from test1 import views
urlpatterns = [
    path('s', views.scaner5, name='scaner5'),
]