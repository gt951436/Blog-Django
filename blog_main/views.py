from django.shortcuts import render

def home(request):
    #return HttpResponse('<h2>This is Blog App Home Page!</h2>')
    return render(request,'home.html')