from django.contrib import admin
from Blogs.models import *

# Register your models here.


@admin.register(User)
class User_Admin(admin.ModelAdmin):
    list_display=['username','first_name','email','biography', 'is_blogger']

@admin.register(Blogs)
class Blogs_Admin(admin.ModelAdmin):
    list_display=['title','description','author','created_at','updated_at']

@admin.register(Comments)
class Comments_Admin(admin.ModelAdmin):
    list_display=['comment','user','blog','created_at','updated_at']

class Blog_Comments_Inline(admin.TabularInline):
    model = Comments
    
class Blogs_Admin(admin.ModelAdmin):
    inlines = [Blog_Comments_Inline]

    class Meta:
        model = Blogs
    
admin.site.register(Blogs_Admin,Blog_Comments_Inline)


# Admin site blog posts records should display the list of associated comments inline (below each blog post).
# TypeError: 'MediaDefiningClass' object is not iterable

