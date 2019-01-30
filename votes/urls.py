from django.contrib import admin
from django.urls import path, include
from .views import (CandidateCreateView, CandidateDetailView, 
					CandidateListView, CandidateUpdateView, 
					VoteCreateView, PositionCreateView, vote)

urlpatterns = [
	path('', CandidateListView.as_view(), name='index'),
	path('<int:pk>/', CandidateDetailView.as_view(), name='candidate_detail'),
	path('create/', CandidateCreateView.as_view(), name='candidate_create'),
	path('<int:pk>/update', CandidateUpdateView.as_view(), name='candidate_update'),
	path('<int:candidate_id>/vote', vote, name='vote'),
	path('position_create/', PositionCreateView.as_view(), name='position_create'),
]
