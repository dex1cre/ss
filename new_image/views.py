from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from .forms import *
from random import choice
from string import ascii_letters

def index(request):
	form = ImageForm()
	return render(request, "new_image/index.html", {
		'form': form,
		})

def send(request):
	if request.method == "POST":
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():

			author_name = request.POST['author']
			try:
				user = User.objects.get(username=author_name)
			except:
				password = ''.join(choice(ascii_letters) for i in range(12))
				user = User.objects.create_user(author_name, author_name+'@mail.ru', password)
				user.save()

			
			post = form.save(commit=False)
			post.author = user
			post.save()

			tags = str(request.POST['tags'])

			tag = ""
			tags = tags + "#"
			for i in tags:
				if i != "#":
					tag = tag + i
				elif i == "#" and tag != "":
					try:
						tag_obj = Tags.objects.get(name=tag)
					except:
						tag = Tags(name=tag)
						tag.save()

						img_tag = ImageTag(tag=tag, image=post)
						img_tag.save()
					else:
						try:
							img_tag_obj = ImageTag.objects.get(tag=tag_obj, image=post)
						except:
							img_tag = ImageTag(tag=tag_obj, image=post)
							img_tag.save()

					tag = ""


			print("Всё получилось!")

		form = ImageForm(request.POST)
		return render(request, "new_image/index.html", {
			'form': form
			})
	else:
		form = ImageForm()
		return render(request, "new_image/index.html", {
			'form': form
			})