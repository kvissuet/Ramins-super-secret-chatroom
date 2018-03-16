from django.conf.urls import url
from . import views

app_name="chatroom"
urlpatterns = [
	# Chatroom homepage
	url(r'^index/', views.index, name='index'),
]