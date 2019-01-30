from django.db import models

# Create your models here.


class Position(models.Model):

	name = models.CharField(max_length=50)
	description = models.TextField()

	class Meta:
		verbose_name = "Position"
		verbose_name_plural = "Positions"

	def __str__(self):
		return self.name

class Candidate(models.Model):

	firstname = models.CharField(max_length=250)
	lastname = models.CharField(max_length=50)
	position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
	birthdate = models.DateField()
	platform = models.TextField()

	class Meta:
		verbose_name = "Candidate"
		verbose_name_plural = "Candidates"
		ordering = ['position__name']


	def __str__(self):
		return "%s %s" % (self.firstname, self.lastname)


class Vote(models.Model):

	candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
	vote_datetime = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Vote"
		verbose_name_plural = "Votes"

	def __str__(self):
		return "%s : %s" % (self.candidate, self.vote_datetime)
