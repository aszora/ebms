from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.

def stuff(request):

    posts = Post.objects.all()
    return render(request, 'market/stuff.html', {})

