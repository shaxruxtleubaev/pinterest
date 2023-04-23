from django.shortcuts import render
from main.models import Category, Post
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth.models import User, AbstractUser
from main.forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'main/home.html', context)

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    category = Category.objects.all()
    context = {
        'post': post,
        'category': category
    }
    return render(request, 'main/post_detail.html', context)

class SignupPageView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'

class TitleDescriptionResulsView(ListView):
    model = Post
    template_name = 'main/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        return object_list

def account(request, pk):
    post = Post.objects.filter(author=request.user)
    account = User.objects.get(username=request.user, id=pk)
    context = {
        'account': account,
        'post': post
    }
    return render(request, 'main/profile.html', context)

def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'main/create_post.html', context)

def post_update(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'main/post_update.html', context)

def post_delete(request, pk):
    post = Post.objects.filter(id=pk)
    post.delete()
    return redirect('/')