from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """Very basic index page"""

    return HttpResponse('Hello, world. Welcome.')