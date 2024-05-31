from django.contrib.auth.views import LoginView, LogoutView
from typing import Any
from django.views.generic.list import ListView
from django.views.generic import TemplateView,CreateView
from .models import *
from django.views.generic.detail import DetailView
from .forms import *
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import *
from django.shortcuts import redirect

class Index(TemplateView):
    template_name = 'home.html'

class Blogs_List_View(ListView):
    template_name = 'blog_lists.html'
    context_object_name = 'blogs'
    paginate_by = 5
    model = Blogs
    ordering = '-created_at'

    
class Bloggers_List_View(ListView):
    template_name = 'bloggers_list.html'
    context_object_name = 'bloggers'
    def get_queryset(self, **kwargs):
        qs = User.objects.filter(is_blogger= True)
        print(qs)
        return qs

class Blogs_Details_View(DetailView):
    template_name = 'blog_details.html'
    model = Blogs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = Blogs.objects.get(pk = self.kwargs['pk'])
        comments = Comments.objects.filter(blog=blog)
        context['blog'] = blog
        context['comments'] = comments
        return context

class Bloggers_Detail_View(DetailView):
    template_name = 'blogger_detail.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blogger = User.objects.get(pk = self.kwargs['pk'])
        blogs = Blogs.objects.filter(author=blogger).order_by('-created_at')
        context['blogger'] = blogger
        context['blogs'] = blogs
        return context
    
class Add_Comment_View(LoginRequiredMixin, CreateView):
    model=Comments
    template_name = "add_comment.html"
    form_class = Add_Comment_Form
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.blog = Blogs.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('blog_details', kwargs = {'pk': self.kwargs['pk']})
    
    def handle_404(self):
        """Handel 404 error."""
        return redirect("login")

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return self.handle_404()
        
        return super().dispatch(request, *args, **kwargs)
    
class Login_View(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        print("========================>>>>>>>>>>>>>>>")
        next_url = self.request.GET.get['next']
        print("========================>>>>>>>>>>>>>>>",next_url)

        print("========================>>>>>>>>>>>>>>>")
        if 'next' in self.request.GET['next']:
            return reverse('next')
        else :
            return reverse('blog')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    

class Logout_View(LogoutView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("blog")
