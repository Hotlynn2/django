# from DjangoProject import NewsApp
from django.shortcuts import render
from .models import News

# Create your views here.

def Home(request):

    context = {
    
        'name' : 'Franklin',
        'height' : 171.5
    }

    return render(request, 'home.html', context)


def NewsP(request):

    obj = News.objects.get(id= 2)

    context = {
        'programming_list' : ['Python', 'PhP', 'Swift', 'JavaScript'],
        'data' : obj
    }

    return render(request, 'news.html', context)


def Contact(request):  

    obj = News.objects.get(id= 1)

    context = {
        
        'new' : obj
    }

    return render(request, 'contact.html')

def Register(request):  

   

    return render(request, 'register.html')