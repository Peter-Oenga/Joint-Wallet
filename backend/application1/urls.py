from django.urls import path
from . import views
from .views import MemberListView, MemberDetailView
from .views import MonthlySavingListCreateAPIView, MonthlySavingDetailAPIView, FineListAPIView, FineDetailAPIView

urlpatterns = [
    path("", views.index, name="index"),
    path("innerpage/", views.inner_page, name="inner_page"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register, name="register"),
    path('api/members/', views.MemberListView.as_view(), name='member-list'),
    path('api/members/<int:pk>/', views.MemberDetailView.as_view(), name='member-detail'),
    path('api/savings/', MonthlySavingListCreateAPIView.as_view(), name='savings-list-create'),
    path('api/savings/<int:pk>/', MonthlySavingDetailAPIView.as_view(), name='savings-detail'),
    path('api/fines/', FineListAPIView.as_view(), name='fines-list'),
    path('api/fines/<int:pk>/', FineDetailAPIView.as_view(), name='fines-detail'),
  ]