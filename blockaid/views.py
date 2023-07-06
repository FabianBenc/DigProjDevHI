from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import ColorForm
from .forms import IsInShopForm
from .forms import ProductForm
from .models import Color
from .models import Product
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.exceptions import MultipleObjectsReturned
import json

"""
class HomePageView(ListView):
    model = Post
    template_name = "home.html"
"""
@login_required
def save_colors(request):
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            color = form.save(commit=False)
            color.user = request.user
            color.save()
            return redirect('home')
    else:
        form = ColorForm()
    
    return render(request, 'save_colors.html', {'form' : form})

def home(request):
    colors = Color.objects.filter(is_in_shop = True)
    print(colors)
    return render(request, "home.html", {'colors' : colors})

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

def my_colors_view(request):
    user = request.user
    colors = Color.objects.filter(user=user)

    context = {
        'colors': colors,
        'form': ProductForm
    }

    return render(request, 'my_colors.html', context)

def post_design(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            color = form.save()  
            color1 = Color.objects.get(id = color.colors.id)
            color1.is_in_shop = True
            color1.save()
        else:
            form = ProductForm()

    return redirect('my_colors')

def remove_design(request):
    if request.method == 'POST':
        form = IsInShopForm(request.POST)

        if form.is_valid():
            color_id = form.cleaned_data['color_id']
            try:
                color = Color.objects.get(id=color_id)
                products = Product.objects.filter(colors=color)
                if products.exists():
                    products.delete()  # Delete all matching products
                    color.is_in_shop = False
                    color.save()
            except (Color.DoesNotExist, MultipleObjectsReturned):
                pass 


    return redirect('my_colors')

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm
    return render(request, 'my_colors.html', {'form': form})

