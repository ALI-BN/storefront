from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(req):
    if req.method == 'POST':
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()  # save the form in the database
            username = form.cleaned_data.get('username')
            messages.success(
                req, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(req, 'users/register.html', {'form': form})


@login_required     # adds funcionalitiy to existing function
def profile(req):
    return render(req, 'users/profile.html')
