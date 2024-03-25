"""_summary_
    """

from django.urls import path
from . import views

urlpatterns = [
    path(route="", view=views.home, name="home"),
    path(route="login", view=views.login_user, name="login"),
    path(route="logout", view=views.logout_user, name="logout"),
    path(route="register", view=views.register_user, name="register"),
    path(route="record/<int:pk>", view=views.user_record, name="record")
]
