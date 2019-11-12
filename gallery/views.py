from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.


def index(request):
	# lol
	images = Image.get_all()
	return render(
		request,
		'gallery/index.html',
		{ 'images': images }
	)
