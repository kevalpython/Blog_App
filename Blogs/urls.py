"""
URL configuration for Blog_App project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('blog/', Index_view.as_view(),name='blog'),
    path('blog/blogs/', Blogs_List_View.as_view(),name='blogs_lists'),
    path('blog/<int:pk>', Blogs_Details_View.as_view(),name='blog_details'),
    path('blog/blogger/<int:pk>', Bloggers_Detail_View.as_view(),name='blogger_details'),
    path('blog/blogger/', Bloggers_List_View.as_view(),name='bloggers_lists'),
    path('blog/<int:pk>/create', Add_Comment_View.as_view(),name='add_comment'),
    path("login/", Login_View.as_view(), name="login"),
    path("logout/", Logout_View.as_view(), name="logout"),
]   
    