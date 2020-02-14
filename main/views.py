from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    postAll = Post.objects.all()
    return render(request, 'main/index.html', {'postAll': postAll})
