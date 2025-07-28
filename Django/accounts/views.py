from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Assign new user to "Regular Users" group
            regular_group, created = Group.objects.get_or_create(name='Regular Users')
            user.groups.add(regular_group)
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})
