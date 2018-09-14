from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    numbers = [1,2,3,4,5]
    name = 'Gabriel'
    args = {'name': name, 'numbers':numbers}
    return render(request, 'accounts/home.html',args)

    # return render(request, 'accounts/login.html',args)

    # return HttpResponse('<em>Home Page!</em>')
