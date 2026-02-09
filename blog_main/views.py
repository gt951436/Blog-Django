from django.shortcuts import render
from blogs.models import Category

def home(request):
    #return HttpResponse('<h2>This is Blog App Home Page!</h2>')
    categories = Category.objects.all()
    print(categories)
    context = {
        'categories':categories,
    }
    return render(request,'home.html',context)