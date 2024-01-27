from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order),
    path('list/', views.order_list),
    path('detail/<int:id>/', views.order_detail),
    path('update/<int:id>/', views.update_order),
    path('delete/<int:id>/', views.delete_order),
]