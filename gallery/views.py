from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Category, Location

# Create your views here.


def index(request):
	print(request.GET)

	if 'category' in request.GET and request.GET['category'] and 'location' in request.GET and request.GET['location']:
		images = Image.by_categories_and_location(request.GET['category'], request.GET['location'])
	elif 'category' in request.GET and request.GET['category']:
		images = Image.by_category(request.GET['category'])
	elif 'location' in request.GET and request.GET['location']:
		images = Image.by_location(request.GET['location'])
	else:
		images = Image.get_all()
		categories = Category.get_all()
		locations = Location.get_all()
		pass
	
	categories = Category.get_all()
	locations = Location.get_all()

	print(request.GET['location'] if 'location' in request.GET and request.GET['location'] else None)
	print(request.GET['category'] if 'category' in request.GET and request.GET['category'] else None)

	return render(
		request,
		'gallery/index.html',
		{
			'images': images,
			'categories': categories,
			'locations': locations,
			'selected_location': int(request.GET['location']) if 'location' in request.GET and request.GET['location'] else None,
			'selected_category': int(request.GET['category']) if 'category' in request.GET and request.GET['category'] else None,
		}
	)
