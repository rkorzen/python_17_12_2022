from django.shortcuts import render

from .forms import PostForm
from .models import Post
# Create your views here.
from django.core.paginator import Paginator

def post_list(request):

    per_page = int(request.GET.get("per_page", 10))
    page_number = request.GET.get("page", 1)

    posts = Post.objects.all()
    paginator = Paginator(posts, per_page)

    page_obj = paginator.get_page(page_number)

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