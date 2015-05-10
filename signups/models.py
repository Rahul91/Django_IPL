from django.db import models

# Create your models here.

class signup(models.Model):
	Name = models.CharField(max_length=120)
	Email = models.EmailField()

	def __unicode__(self):
		return self.Email

class ipl_scores(models.Model):
	Detail = models.TextField(max_length=200)
	Score1 = models.CharField(max_length=60)
	Score2 = models.CharField(max_length=60)

	def __unicode__(self):
		return self.Detail

