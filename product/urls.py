from django.urls import path
from . import views

urlpatterns = [
    path('api', views.product_list),
    path('api/<int:id>', views.product_detail),
    path('api/add', views.add_product),
    path('api/update/<int:id>', views.update_product),
    path('api/delete/<int:id>', views.delete_product),

    # CBV
    path('cbv', views.PostListAPI.as_view()),
]
