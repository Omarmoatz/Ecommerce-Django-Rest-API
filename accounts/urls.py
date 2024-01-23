from django.urls import path
from . import views


urlpatterns = [
    path('signup', views.signup_api ),
    path('get_info', views.user_info )
]
