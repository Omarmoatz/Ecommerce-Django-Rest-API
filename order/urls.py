from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order),
    path('list/', views.order_list),
    path('detail/<int:id>/', views.order_detail),
]