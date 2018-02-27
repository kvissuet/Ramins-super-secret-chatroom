from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib import messages
from django.db.models import F

from .forms import SignUpForm, ProfileForm, UserForm

# Create your views here.
def logout_view(request):
	"""Log the user out."""
	logout(request)
	return HttpResponseRedirect(reverse('intro:index'))
	
def register(request):
	"""Register a new user."""
	if request.method != 'POST':
		# Display blank registration form.
		form = UserCreationForm()
	else:
		# Process completed form.
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			# Log the user in and then redirect to home page.
			authenticated_user = authenticate(username=new_user.username,
				password=request.POST['password1'])
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('intro:index'))
	context = {'form': form}
	return render(request, 'users/register.html', context)
	
def profile(request):
	#Look and update profile page.
	if request.method != 'POST':
		# Display blank registration form.
		form = UserCreationForm()
	else:
		# Process completed form.
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			# Log the user in and then redirect to home page.
			authenticated_user = authenticate(username=new_user.username,
				password=request.POST['password1'])
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('intro:index'))
	context = {'form': form}
	return render(request, 'users/Profile.html', context)
	

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.shift = form.cleaned_data.get('shift')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('intro:index')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})
    
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('users:update_profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        u=request.user
        prime_mult=u.profile.prime_1*u.profile.prime_2
    return render(request, 'users/Profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'mult':prime_mult
    })