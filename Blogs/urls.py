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

from django.urls import path

from .views import (AddCommentView, BloggersDetailView, BloggersListView,
                    BlogsDetailsView, BlogsListView, IndexView, LoginUserView,
                    LogoutUserView,SignUpView,AddBlogView,EditBlogView,DeleteBlogView,AllUserView,UserActivationView)

urlpatterns = [
    path("blog/", IndexView.as_view(), name="blog"),
    path("blog/blogs/", BlogsListView.as_view(), name="blogs_lists"),
    path("blog/<int:pk>", BlogsDetailsView.as_view(), name="blog_details"),
    path("blog/blogger/<int:pk>", BloggersDetailView.as_view(), name="blogger_details"),
    path("edit/blog/<int:pk>", EditBlogView.as_view(), name="edit_blog"),    
    path("delete/blog/<int:pk>", DeleteBlogView.as_view(), name="delete_blog"),
    path("active/user/<int:pk>", UserActivationView.as_view(), name="active_deactive_user"),
    path("blog/blogger/", BloggersListView.as_view(), name="bloggers_lists"),
    path("users/", AllUserView.as_view(), name="all_user"),
    path("add/blog/", AddBlogView.as_view(), name="add_blog"),
    path("blog/<int:pk>/create", AddCommentView.as_view(), name="add_comment"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
]

