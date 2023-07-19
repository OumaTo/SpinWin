from django.shortcuts import HttpResponse, redirect,render

def home(request):
    return HttpResponse('Hello There It worked')

