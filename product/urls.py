from django.urls import path
from . import views

urlpatterns = [
    path('api', views.product_list),
    path('api/<int:id>', views.product_detail)
]
