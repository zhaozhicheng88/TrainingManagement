from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', user_views.index, name='index'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
