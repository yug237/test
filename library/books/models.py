from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	author = models.CharField(max_length=100)
	image = models.ImageField(default=None)
	rating = models.IntegerField(default='2')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk' : self.pk})