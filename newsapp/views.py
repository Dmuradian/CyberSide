from django.shortcuts import render
from django.http import HttpResponse
# from .models import Person

def home(request):
    return render(request, 'newsapp/home.html')


def user(request):
    return render(request, 'newsapp/user.html')