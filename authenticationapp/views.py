from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import ProfileForm

# Home page view
def home(request):
    return render(request, 'home.html')

# Sign up view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Profile view
@login_required
def profile(request):
    return render(request, 'profile.html')

# Edit profile view
@login_required
def edit_profile(request):
    profile = request.user.userprofile  # requires related_name='userprofile' in your model
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})
