"""_summary_

    Returns:
        _type_: _description_
    """


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
        username: str = request.POST.get('username', default={})
        password: str = request.POST.get('password', default={})

        # Auth
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            messages.success(request=request, message="Login Successful")
            return redirect('home')

        if user is None:
            messages.success(request=request, message="Oops! Something went wrong...Try again if you dare...")
            return redirect('home')

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

    return render(request=request, template_name='register.html')