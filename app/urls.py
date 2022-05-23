
from django.urls import path
from .import views

urlpatterns = [
    path("", views.login_user, name="login"),
    path("login", views.login_user, name="login"),
    path("register", views.register, name="register"),
    path("index", views.index, name="index"),
    path("create_resume", views.create_resume, name="create_resume"),
    path("resume", views.resume, name="resume"),
]
