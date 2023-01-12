from django.shortcuts import render
from .models import Post

# Create your views here.
def index(requset): 
    posts = Post.objects.order_by('-pk')
    return render(requset, 'blog/index.html',{'posts':posts,})

def single_post_page(request, value):
    post = Post.objects.get(pk=value)
    
    return render(request, 'blog/single_post_page.html',
                  {'post':post,})