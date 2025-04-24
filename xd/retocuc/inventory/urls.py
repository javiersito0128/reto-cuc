from django.urls import path
from .views import login_view, inventory_list, logout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('inventory/', inventory_list, name='inventory_list'),
    path('logout/', logout_view, name='logout'),
]