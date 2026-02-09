from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def posts_by_category(request, category_id):
    #fetch the posts of the category with the ID 'category_id'
    posts = Blog.objects.filter(status="Published",category = category_id)
    context = {
        'posts': posts,
    }
    return render(request,'posts_by_category.html',context)