from django.urls import path
from . import views
from .views import MemberListAPIView, MemberDetailAPIView

urlpatterns = [
    path("", views.index, name="index"),
    path("innerpage/", views.inner_page, name="inner_page"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register, name="register"),
    path('api/members/', views.MemberListAPIView.as_view(), name='member-list'),
    path('api/members/<int:pk>/', views.MemberDetailAPIView.as_view(), name='member-detail'),
  ]