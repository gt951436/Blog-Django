from django.shortcuts import render
from blogs.models import Category,Blog

def home(request):
    #return HttpResponse('<h2>This is Blog App Home Page!</h2>')
    categories = Category.objects.all()
    #print(categories)
    featured_posts = Blog.objects.filter(is_featured = True)
    print(featured_posts)
    context = {
        'categories':categories,
        'featured_posts':featured_posts,
    }
    return render(request,'home.html',context)