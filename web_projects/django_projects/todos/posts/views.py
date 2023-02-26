from django.shortcuts import render

from .forms import PostForm
from .models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.all()

    return render(
        request,
        "posts/list.html",
        {"posts": posts}
    )

def post_details(request, id):
    post = Post.objects.get(id=id)
    form = PostForm()
    return render(
        request,
        "posts/details.html",
        {"post": post, "form": form}
    )