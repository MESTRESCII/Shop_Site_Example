"""exampleSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('products/', views.products, name="products"),
    path('contact/', views.contact, name="contact"),
    path("accounts/profile/", views.ProfileView.as_view(), name='profile'),

    # Django Authentication Paths
    path('accounts/login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Django Register Paths
    path('accounts/register/', views.register_request, name='register'),

    # Django Password Recover Path
    path('passwordRecovery/password_reset/',
         views.password_reset_request,
         name="password_reset"),
    path('passwordRecovery/password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name="passwordRecovery/password_reset_done.html"),
         name="password_reset_done"),
    path('passwordRecovery/<uid>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="passwordRecovery/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path('passwordRecovery/password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="passwordRecovery/password_reset_complete.html"),
         name="password_reset_complete"),

]
