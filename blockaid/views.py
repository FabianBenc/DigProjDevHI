from django.views.generic import ListView, CreateView  # new
from django.urls import reverse_lazy  # new
from .forms import PostForm  # new
from .models import Post
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

"""
class HomePageView(ListView):
    model = Post
    template_name = "home.html"
"""

class CreatePostView(CreateView):  # new
    model = Post
    form_class = PostForm
    template_name = "post.html"
    success_url = reverse_lazy("home")

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created successfully. You can log in.')
            return redirect("login")
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)