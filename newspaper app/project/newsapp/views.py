from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm, CategoryForm, ArticleForm
from .models import Article, Category
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
import json
from django.http import HttpResponse
from typing import *
from django.contrib import messages



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'newsapp/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:
                return redirect('adminpage')
            else:
                return redirect('homepage')
    else:
        form = LoginForm()
    return render(request, 'newsapp/login.html', {'form': form})

def homepage(request):
    categories = Category.objects.all()
    return render(request, 'newsapp/homepage.html', {'categories':categories})

def adminpage(request):
    categories = Category.objects.all()
    articles = Article.objects.all()
    return render(request, 'newsapp/adminpage.html', {'categories':categories, 'articles':articles})

def user_is_admin(user):
    return user.is_superuser

@user_passes_test(user_is_admin)
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully.')
        else:
            form = CategoryForm()
    return render(request, 'newsapp/addCategory.html', {'form': form})




def get_categories(request) -> JsonResponse:
    if request.method == 'GET':
        return JsonResponse({
            'categories': [
                Category.to_dict()
                for Category in Category.objects.all()
            ]
        })
    return JsonResponse({
        'new': 'updated'
    })  

@user_passes_test(user_is_admin)
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article added successfully.')
        else:
            form = ArticleForm()
    
    # categories = Category.objects.all()  # Assuming you have a Category model
    return render(request, 'newsapp/addArticle.html', {'form': form})



def get_articles(request: Any) -> JsonResponse:
    if request.method=='GET':
        return JsonResponse({
            'articles': [
                Article.to_dict()
                for Article in Article.objects.all()
            ]
        })
    return JsonResponse({
        'new': 'updated'
    }) 

def get_articles_by_category(request):
    selected_category_id = request.GET.get('selected_category')
    if selected_category_id:
        selected_category = Category.objects.get(pk=selected_category_id)
        articles = Article.objects.filter(category=selected_category)
    else:
        articles = []

    categories = Category.objects.all()
    return render(request, 'newsapp/homepage.html', {'categories': categories, 'articles': articles})