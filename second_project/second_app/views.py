from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<em>My Second Resonse as it was changed</em>')

# Create your views here.
