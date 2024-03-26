"""_summary_
    """

from django.urls import path
from . import views

urlpatterns = [
    path(route="", view=views.home, name="home"),
    path(route="login", view=views.login_user, name="login"),
    path(route="logout", view=views.logout_user, name="logout"),
    path(route="register", view=views.register_user, name="register"),
    path(route="record/<int:pk>", view=views.user_record, name="record"),
    path(route="delete/<int:pk>", view=views.delete_record, name="delete_record"),
    path(route="create_record", view=views.create_record, name="create_record"),
    path(route="update_record/<int:pk>", view=views.update_record, name="update_record"),
]
