from django.shortcuts import render
from .models import *
from new_image.models import *

def see_image(request, num):
	image = Image.objects.get(id=num)
	image_tag = ImageTag.objects.filter(image=image)

	return render(request, 'voting/index.html', {
		'image': image,
		'image_tag': image_tag,
		})
