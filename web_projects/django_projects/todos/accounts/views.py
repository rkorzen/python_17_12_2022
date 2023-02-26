from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserProfileForm, NewUserForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail


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


def user_registration(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You are registered")
            send_mail(
                "Subject",
                "Message.",
                "from@example.com",
                ["john@example.com", "jane@example.com"],
            )
            return redirect("home")
        messages.error(request, "Something wrong")

    form = NewUserForm()
    return render(
        request, template_name="registration/register.html", context={"form": form}
    )
