from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from common.views import paginate
from .forms import PostForm
from .models import Post


# Create your views here.


@login_required
def post_list(request):

    if request.method == "POST":
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

    form = PostForm()
    page_obj = paginate(request, Post)

    return render(request, "posts/list.html", {"page_obj": page_obj, "form": form})


def post_details(request, id):
    post = Post.objects.get(id=id)
    form = PostForm()
    return render(request, "posts/details.html", {"post": post, "form": form})
