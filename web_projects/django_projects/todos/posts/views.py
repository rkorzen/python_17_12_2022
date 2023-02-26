from django.shortcuts import render

from common.views import paginate
from .forms import PostForm
from .models import Post


# Create your views here.


def post_list(request):

    page_obj = paginate(request, Post)

    return render(
        request,
        "posts/list.html",
        {"page_obj": page_obj}
    )


def post_details(request, id):
    post = Post.objects.get(id=id)
    form = PostForm()
    return render(
        request,
        "posts/details.html",
        {"post": post, "form": form}
    )
