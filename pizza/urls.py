from django.urls import path
from . import views

urlpatterns = [
    path('', views.order, name='order'), # order pizza route ("http://localhost:8000/order")
    path('<int:pk>/', views.edit_order, name='edit_order') 
    # UPDATE (edit) order in db, path('pizzas/', views.pizzas, name='pizzas')
]


