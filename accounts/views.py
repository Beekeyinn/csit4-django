from django.shortcuts import redirect, render

from accounts.forms import UserCreationForm
from profiles.models import UserProfile


# Create your views here.
def register(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "accounts/register.html", {"form": form})
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect("login")
        else:
            return render(request, "accounts/register.html", {"form": form})


from django.contrib.auth import authenticate
from django.contrib.auth import login as _login

from accounts.forms import LoginForm


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "accounts/login.html", {"form": form})
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                email=form.cleaned_data.get("email"),
                password=form.cleaned_data.get("password"),
            )
            if user:
                _login(request, user)
                return redirect("post-list")
            else:
                return render(
                    request,
                    "accounts/login.html",
                    {"form": form, "message": "User does not exist."},
                )
        else:
            return render(request, "accounts/login.html", {"form": form})
