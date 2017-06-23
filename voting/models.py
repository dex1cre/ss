from django.db import models

class Vote(models.Model):
	image = models.ForeignKey('new_image.Image')
	user = models.ForeignKey('auth.User')
	rating = models.IntegerField()

	def __str__(self):
		return str(image) + "..." + str(user) + "..." + str(rating)