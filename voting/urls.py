from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<num>\d+)/$', views.see_image, name="see_image"),
	
]