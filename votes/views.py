from django.shortcuts import render
from django.views.generic.list import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Candidate, Votes, Position
# Create your views here.
class CandidateListView(ListView):
	model = Candidate
	template_name = "votes/index.html"
	context_object_name = 'candidates'


class CandidateDetailView(DetailView):
	model = Candidate
	template_name = "votes/candidate_detail.html"
	context_object_name = 'candidate'


class CandidateCreateView(CreateView):
	model = Candidate
	template_name = "votes/candidate_create.html"
	fields = ['firstname', 'lastname', 'position', 'birthdate', 'platform']

	def get_success_url(self):
		return reverse('index')

class CandidateUpdateView(UpdateView):
	model = Candidate
	template_name = "votes/candidate_update.html"
	fields = ['firstname', 'lastname', 'position', 'birthdate', 'platform']

	def get_success_url(self):
		return reverse('index')
    	#return reverse('post-detail', kwargs={'pk': self.kwargs['post_id']})

class PositionCreateView(CreateView):
	model = Position
	template_name = "votes/position_create.html"
	fields = ['name', 'description']

	def get_success_url(self):
		return reverse('index')

class VoteCreateView(CreateView):
	model = Vote
	template_name = "votes/vote.html"
	fields = ['candidate']

	def get_success_url(self):
		return reverse('index')