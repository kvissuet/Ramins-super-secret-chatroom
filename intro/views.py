from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from .RSA import RSA_encryption
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
	"""The home page for Learning Log"""
	return render(request, 'intro/index.html')
	
def topics(request):
	"""Show all topics."""
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'intro/topics.html', context)
	
def topic(request, topic_id):
	"""Show a single topic and all its entries."""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'intro/topic.html', context)

@login_required
def new_topic(request):
	"""Add a new topic."""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = TopicForm()
	else:
		# POST data submitted; process data.
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('intro:topics'))

	context = {'form': form}
	return render(request, 'intro/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
	"""Add a new entry for a particular topic."""
	topic = Topic.objects.get(id=topic_id)
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = EntryForm()
	else:
		# POST data submitted; process data.
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.owner = request.user
			RSA_modulo=request.user.profile.RSA_n
			RSA_public=request.user.profile.RSA_private_key
			text=form.cleaned_data.get('text')
			new_entry.RSA_modulo=RSA_modulo
			new_entry.RSA_public=RSA_public
			new_entry.encrypted_text=RSA_encryption(RSA_modulo,RSA_public,text)
			new_entry.save()
			return HttpResponseRedirect(reverse('intro:topic',
				args=[topic_id]))
	context = {'topic': topic, 'form': form}
	return render(request, 'intro/new_entry.html', context)
	
def edit_entry(request, entry_id):
	"""Edit an existing entry."""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	# Make sure the entry belongs to the current user.
	if entry.owner != request.user:
		raise Http404	
	
	if request.method != 'POST':
		# Initial request; pre-fill form with the current entry.
		form = EntryForm(instance=entry)
	else:
		# POST data submitted; process data.
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('intro:topic',
				args=[topic.id]))
	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'intro/edit_entry.html', context)
	
	
def decrypt_entry(request, entry_id):
	"""decrypt an existing entry."""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	# Make sure the entry belongs to the current user.

	if request.method != 'POST':
		# Initial request; pre-fill form with the current entry.
		form = EntryForm(instance=entry)
	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'intro/decrypt_entry.html', context)