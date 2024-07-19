from django.urls import path
from product import views
urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('all_product/', views.all_product, name='all_product'),
    path('edit_product/<int:id>', views.edit_product, name='edit_product'),
    path('add_category/', views.add_category, name='add_category'),
    path('select_category/<int:id>', views.select_category, name='select_category'),
]