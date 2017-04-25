from django.shortcuts import render
from blog.models import *

# Create your views here.

def index(request):
    context = {
        'Blog': Blog.objects.all(),
    }
    return render(request, "index.html", context)