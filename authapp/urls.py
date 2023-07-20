from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from authapp.views import login_view, logout_view

app_name = "authapp"

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
]
