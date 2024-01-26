from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    reset_password_token = models.CharField(max_length=50,blank=True,default="")
    reset_password_expire = models.DateTimeField(blank=True, null=True)

    
