"""Defines URL patterns for users"""
from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
app_name="users"
urlpatterns = [
	# Login page
	url(r'^login/$', login, {'template_name': 'users/login.html'},
		name='login'),
	
	# Logout page
	url(r'^logout/$', views.logout_view, name='logout'),
		
	# Registration page
	url(r'^register/$', views.register, name='register'),
	
	#New Registration page
	url(r'^signup/$', views.signup, name='signup'),
	
	#Update Profile page
	url(r'^update_profile/$', views.update_profile, name='update_profile'),
	
	#Profile page
	url(r'^profile/$', views.profilepage, name='profile'),
	
	#User page
	url(r'^users/$', views.users, name='users'),
]