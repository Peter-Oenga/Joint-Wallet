from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("innerpage", views.inner_page, name="inner_page"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("login/", views.login_user, name="login"),
     path("logout/", views.logout_user, name="logout"),
]