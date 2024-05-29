from django.contrib import admin
from Blogs.models import *

# Register your models here.

@admin.register(User)
class User(admin.ModelAdmin):
    list_display=['username','first_name','email','biography', 'is_blogger']

@admin.register(Blogs)
class Post(admin.ModelAdmin):
    list_display=['title','description','author','created_at','updated_at']

@admin.register(Comments)
class Post(admin.ModelAdmin):
    list_display=['comment','user','blog','created_at','updated_at']
