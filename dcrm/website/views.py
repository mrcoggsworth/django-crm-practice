"""_summary_

    Returns:
        _type_: _description_
    """

from .forms import SignUpForm

from typing import Any, Dict, List, Optional, Union

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request: HttpRequest) -> HttpResponse:
    """_summary_

    Args:
        request (HttpRequest): _description_

    Returns:
        HttpResponse: _description_
    """

    if request.method == "POST":
        username: str = request.POST.get("username", default={})
        password: str = request.POST.get("password", default={})

        # Auth
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            messages.success(request=request, message="Login Successful")
            return redirect("home")

        if user is None:
            messages.success(
                request=request,
                message="Oops! Something went wrong...Try again if you dare...",
            )
            return redirect("home")

        print("Its a POST REQUEST!")

    if request.method == "GET":
        return render(request=request, template_name="home.html")


def login_user(request: HttpRequest) -> HttpResponse:
    """_summary_

    Args:
        request (HttpRequest): _description_

    Returns:
        HttpResponse: _description_
    """

    pass


def logout_user(request: HttpRequest) -> HttpResponse:
    """_summary_

    Args:
        request (HttpRequest): _description_

    Returns:
        HttpResponse: _description_
    """

    logout(request=request)
    messages.success(request=request, message="You have been properly logged out...")
    return redirect(to="home")


def register_user(request: HttpRequest) -> HttpResponse:
    """_summary_

    Args:
        request (HttpRequest): _description_

    Returns:
        HttpResponse: _description_
    """
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username: str = form.cleaned_data.get("username")
            password: str = form.cleaned_data.get("password1")

            user: Optional[Any | None] = authenticate(
                username=username, password=password
            )
            login(request=request, user=user)

            messages.success(
                request=request, message="You have been successfully registered..."
            )
            return redirect(to="home")

        # messages.error(request=request, message="Oops! Something went wrong...")
        # return redirect(to="register")

    if request.method == "GET":
        form = SignUpForm()
        return render(
            request=request, template_name="register.html", context={"form": form}
        )

    return render(request=request, template_name="register.html", context={"form": form})
