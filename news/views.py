from django.shortcuts import render, render_to_response
from news.models import *


# Create your views here.

def index(request):
    context = {
        'News': News.objects.all(),
    }
    return render(request, "index.html", context)
