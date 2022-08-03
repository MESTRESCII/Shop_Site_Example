from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def index(request: HttpRequest):
    return render(request, 'index.html')


def about(request: HttpRequest):
    return render(request, 'about.html')


def contact(request: HttpRequest):
    return render(request, 'contact.html')


def products(request: HttpRequest):
    return render(request, 'products.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect("index")
        messages.error(request, "Fail to Register new User")
    form = NewUserForm()
    return render(request=request, template_name="accounts/register.html", context={"register_form": form})


def password_reset_request():
    return None


class ProfileView(LoginRequiredMixin, TemplateView):

    template_name = "accounts/profile.html"
