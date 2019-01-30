from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Candidate, Vote, Position
from django.urls import reverse

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
		return reverse('candidate_detail', kwargs={'pk': self.kwargs['pk']})
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


def vote(request, candidate_id):
	# if request.method == 'POST':
	candidate = Candidate.objects.get(id=candidate_id)
	Vote.objects.create(candidate=candidate)
	return redirect('index')

# def comment(request, post_id):
# 	post = Post.objects.get(id=post_id)
# 	context = {}

# 	if request.method == 'POST':
# 		form = CommentForm(request.POST)
# 		if form.is_valid():
# 			new_comment = form.save(commit=False)
# 			new_comment.post = post
# 			new_comment.save()
# 			return redirect('post-detail', post_id)
# 		else:
# 			context['form'] = form
# 			return render(request, 'post/create_comment.html', context)
# 	else:
# 		form = CommentForm()
# 		context['form'] = form
# 		return render(request, 'post/create_comment.html', context)