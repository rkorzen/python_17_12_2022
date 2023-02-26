from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserProfileForm
from django.contrib.auth import authenticate, login


def user_profile_view(request):

    if not request.user.is_authenticated:
        return HttpResponse("Nie możesz tu byc")

    if request.method == "POST":
        form = UserProfileForm(
            instance=request.user.userprofile, data=request.POST, files=request.FILES
        )
        if form.is_valid():
            form.save()

    form = UserProfileForm(instance=request.user.userprofile)
    return render(request, "accounts/profile.html", {"form": form})


def login_view(request):

    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        ...
    else:
        ...
