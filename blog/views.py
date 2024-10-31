from django.shortcuts import render, get_list_or_404
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts})


def post_details(request, id):
    post = get_list_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post':post})


