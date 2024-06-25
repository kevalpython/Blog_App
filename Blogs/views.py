"""
This module contains views for passing data to the frontend or user.
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import AddCommentForm, SignUpForm, AddBlogForm, Edit_BlogForm
from .models import Blogs, Comments, User


class IndexView(TemplateView):
    """
    This module renders the home template to the user.
    """

    template_name = "home.html"


class BlogsListView(ListView):
    """
    This module renders the Blog template to the user and shows the lists of blogs in the HTML file.

    Returns:
        Pagination of 5 blogs, with the latest blog displayed first and the rest following.
    """

    template_name = "blog_lists.html"
    context_object_name = "blogs"
    paginate_by = 5
    model = Blogs
    ordering = "-created_at"


class BloggersListView(ListView):
    """
    This module renders the Bloggers template to the user and shows the lists of bloggers in the HTML file.
    """

    template_name = "bloggers_list.html"
    context_object_name = "bloggers"

    def get_queryset(self):
        """
        This get_queryset method is for sending all bloggers to show the user.

        Returns:
            All bloggers.
        """
        qs = User.objects.filter(is_blogger=True)
        return qs


class BlogsDetailsView(DetailView):
    """
    This module is used to show details for a specific blog.
    """

    template_name = "blog_details.html"
    model = Blogs

    def get_context_data(self, **kwargs):
        """
        This get_context_data method is used to display data in the HTML template.

        Returns:
            Blog details and its comments.
        """
        context = super().get_context_data(**kwargs)
        blog = Blogs.objects.get(pk=self.kwargs["pk"])
        context["blog"] = blog
        context["comments"] = Comments.objects.filter(blog=blog)
        return context


class BloggersDetailView(DetailView):
    """
    this module is use for showing detail of specific bloggers
    """

    template_name = "blogger_detail.html"
    model = User

    def get_context_data(self, **kwargs):
        """
        This get_context_data method is use for display data in html template

        kwargs : return the object of the model

        it return the bloggers details  and their blogs
        """
        context = super().get_context_data(**kwargs)
        blogger = User.objects.get(pk=self.kwargs["pk"])
        blogs = Blogs.objects.filter(author=blogger).order_by("-created_at")
        context["blogger"] = blogger
        context["blogs"] = blogs
        return context


class AddCommentView(LoginRequiredMixin, CreateView):
    """
    This module is used to add comments to a blog, and the user should be logged in.

    CreateView is used to create data in the model.
    LoginRequiredMixin is used to check if the user is logged in or not.
    """

    model = Comments
    template_name = "add_comment.html"
    form_class = AddCommentForm

    def form_valid(self, form):
        """
        This method is used to create data in the model.

        Args:
            form: This argument is used to get data from the form.

        Returns:
            Returns super class's form_valid method after setting the user and blog instance.

        After submitting the data, it redirects to the blog details page.
        """
        form.instance.user = self.request.user
        form.instance.blog = Blogs.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Shows the error if it occurs in the form.
        """
        return super().form_invalid(form)

    def get_success_url(self):
        """
        Redirects to the blog details page.
        """
        return reverse_lazy("blog_details", kwargs={"pk": self.kwargs["pk"]})

    def handle_404(self):
        """
        Handles 404 error by redirecting to the login page.
        """
        return redirect("login")

    def dispatch(self, request, *args, **kwargs):
        """
        Handles dispatching of requests.
        """
        if not request.user.is_authenticated:
            return self.handle_404()
        return super().dispatch(request, *args, **kwargs)


class AddBlogView(LoginRequiredMixin, CreateView):
    template_name = "add_blog.html"
    model = Blogs
    form_class = AddBlogForm
    success_url = reverse_lazy("blog")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class EditBlogView(LoginRequiredMixin, UpdateView):
    model = Blogs
    form_class = Edit_BlogForm
    template_name = "edit_blog.html"

    def get_success_url(self):

        blog_id = self.object.id if self.object else None
        return reverse_lazy("blog_details", kwargs={"pk": blog_id})

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):

        return super().form_invalid(form)


class DeleteBlogView(LoginRequiredMixin, DeleteView):
    model = Blogs
    success_url = reverse_lazy("blogs_lists")
    template_name = "blog_details.html"

    def post(self, request, *args, **kwargs):

        blog_id = self.request.POST.get("pk")
        print(blog_id)
        if blog_id:
            blog = Blogs.objects.filter(id=blog_id).first()
            if blog:
                blog.delete()

        return super().post(request, *args, **kwargs)


class AllUserView(LoginRequiredMixin, ListView):

    template_name = "all_user.html"
    context_object_name = "users"
    model = User
    ordering = "-date_joined"


class UserActivationView(LoginRequiredMixin,DetailView):
    model = User
    template_name = "all_user.html"

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()
        else:
            user.is_active = False
            user.save()
        return redirect(reverse("all_user"))

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        print(pk)
        return self.model.objects.get(pk=pk)


class SignUpView(CreateView):
    template_name = "signup.html"
    model = User
    form_class = SignUpForm

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data["password"]
        user.is_blogger = True
        user.set_password(password)
        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirects to the blog details page.
        """
        return reverse_lazy("login")


class LoginUserView(LoginView):
    """
    This class handles user login functionality.

    Attributes:
        template_name (str): The name of the template to render the login page.
        redirect_authenticated_user (bool): Indicates whether to redirect authenticated users. Default is True.
    """

    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        """
        Get the URL to redirect to after a successful login.

        Returns:
            str: The URL to redirect to.
        """
        return reverse("blog")

    def form_invalid(self, form):
        """
        Handles invalid form submission.

        Args:
            form (Form): The form instance with invalid data.

        Returns:
            HttpResponse: A response with the rendered login page and form data.
        """
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))


class LogoutUserView(LogoutView):
    """
    This class handles user logout functionality.

    Attributes:
        redirect_authenticated_user (bool): Indicates whether to redirect authenticated users. Default is False.
    """

    redirect_authenticated_user = True

    def get_success_url(self):
        """
        Get the URL to redirect to after a successful logout.

        Returns:
            str: The URL to redirect to.
        """
        return reverse_lazy("blog")
