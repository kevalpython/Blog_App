"""
This module contains Django model definitions.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    A custom user model representing a user of the application.
    """

    biography = models.CharField(max_length=255, blank=True, null=True)
    is_blogger = models.BooleanField(default=False)
    def __str__(self):
        """
        Return the username as the string representation of the user.
        """
        return str(self.username)


class Blogs(models.Model):
    """
    A model representing a blog post.
    """

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """
        Return the title of the blog post as its string representation.
        """
        return str(self.title)

    def get_absolute_url(self):
        """
        Return the absolute URL of the blog post.
        """
        return f"/blog/{self.id}/"


class Comments(models.Model):
    """
    A model representing a comment on a blog post.
    """

    comment = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return the content of the comment as its string representation.
        """
        return str(self.comment)
