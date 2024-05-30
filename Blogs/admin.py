from django.contrib import admin
from Blogs.models import *

# Register your models here.

@admin.register(User)
class User_Admin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'email', 'biography', 'is_blogger']

class Blog_Comments_Inline(admin.TabularInline):
    model = Comments
    extra = 0

@admin.register(Blogs)
class Blogs_Admin(admin.ModelAdmin):
    list_display = ['title', 'truncated_description', 'author', 'created_at', 'updated_at']
    def truncated_description(self, obj):
        if len(obj.description) > 75:
            return obj.description[:75] + '...'
        else :
            return obj.description
    inlines = [Blog_Comments_Inline]

@admin.register(Comments)
class Comments_Admin(admin.ModelAdmin):
    list_display = ['truncated_comment', 'user', 'blog', 'created_at', 'updated_at']

    def truncated_comment(self, obj):
        if len(obj.comment) > 75:
            return obj.comment[:75] + '...'
        else :
            return obj.comment