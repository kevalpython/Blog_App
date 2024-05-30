from django.contrib import admin
from Blogs.models import *

# Register your models here.


@admin.register(User)
class User_Admin(admin.ModelAdmin):
    list_display=['username','first_name','email','biography', 'is_blogger']

class Blog_Comments_Inline(admin.TabularInline):
    model = Comments

@admin.register(Blogs)
class Blogs_Admin(admin.ModelAdmin):
    list_display=['title','description','author','created_at','updated_at']
    inlines = [Blog_Comments_Inline]

@admin.register(Comments)
class Comments_Admin(admin.ModelAdmin):
    list_display=['comment','user','blog','created_at','updated_at']
