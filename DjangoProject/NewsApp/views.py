from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def Home(request):

    context = {
    
        'name' : 'Franklin'
    }

    return render(request, 'home.html', context)


def News(request):

    context = {
        'programming_list' : ['Python', 'PhP', 'Swift', 'JavaScript']
    }

    return render(request, 'news.html', context)


def Contact(request):
    return render(request, 'contact.html')
