from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
	user = models.ForeignKey(User, null=True, related_name="ranking_card", on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return '%s %s' % ('Page URL:', self.name)