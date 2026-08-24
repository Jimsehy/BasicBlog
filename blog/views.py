from django.shortcuts import render, redirect
from blog.models import Category, Post


# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def categories(request):
    categories = Category.objects.all()
    return render(request,
                  'blog/categories.html',
                  {'categories': categories})

def posts(request):
    posts = Post.objects.all()
    return render(request,
                  'blog/posts.html',
                  {'posts': posts})

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    return render(request,
                  'blog/category_detail.html',
                  {'category': category})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request,
                  'blog/category_detail.html',
                  {'post': post})

def category_create(request):
    category_name = request.POST['name']
    category = Category.objects.create(name=category_name)
    return redirect('categories')

def category_update(request, category_id):
    category = Category.objects.get(id=category_id)
    category.name = request.POST['name']
    category.save()
    return redirect('categories')

def category_delete(request):
    category_id = request.POST['category_id']
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('categories')
