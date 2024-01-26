from django.urls import path
from . import views

urlpatterns = [
    # Product API
    path('api', views.product_list),
    path('api/<int:id>', views.product_detail),
    path('api/add', views.add_product),
    path('api/update/<int:id>', views.update_product),
    path('api/delete/<int:id>', views.delete_product),

    # Review API
    path('review/add/<int:id>/', views.create_review),
    path('review/<int:id>/delete/<int:pk>/', views.delete_review),

    # CBV
    path('cbv/', views.PostListAPI.as_view()),
]
