from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<em>My Second Resonse</em>')

# Create your views here.
