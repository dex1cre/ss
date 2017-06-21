from django.db import models

# class User(models.Model):
# 	name = models.CharField(max_length=200)

# 	def __str__(self):
# 		return self.name

class Image(models.Model):
	author = models.ForeignKey('auth.User')
	image = models.ImageField(upload_to="images", verbose_name="Imagesss", blank=True)
	description = models.CharField(max_length=30)

	def __str__(self):
		return str(self.author)