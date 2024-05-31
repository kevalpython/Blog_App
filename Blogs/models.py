from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import User

class User(AbstractUser):
    biography = models.CharField(max_length = 255, blank=True, null=True)
    is_blogger   = models.BooleanField(default=False)

    def __str__(self):
            return self.username
    


class Blogs(models.Model):
    title = models.CharField(max_length = 64)
    description = models.CharField(max_length = 255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.id}/"

class Comments(models.Model):
    comment= models.CharField(max_length=255,null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.comment

