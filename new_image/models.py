from django.db import models

class Image(models.Model):
	author = models.ForeignKey('auth.User')
	image = models.ImageField(upload_to="images", verbose_name="Изображение", blank=True)
	description = models.CharField(verbose_name='Короткое описание', max_length=30)

	def __str__(self):
		return str(self.author)

class Tags(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class ImageTag(models.Model):
	tag = models.ForeignKey('Tags')
	image = models.ForeignKey('Image')

	def __str__(self):
		return str(self.tag) + "->" + str(self.image)