from django.shortcuts import render
from .models import *
from .forms import *

def index(request):
	form = ImageForm()
	return render(request, "new_image/index.html", {
		'form': form
		})

def send(request):
	form = ImageForm()
	return render(request, "new_image/index.html", {
		'form': form
		})