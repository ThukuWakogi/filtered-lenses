from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.


class ImageTestClass(TestCase):
	def setUp(self):
		self.test_location = Location(location_name='Test Location')
		self.test_location.save_location()
		self.test_category = Category(category_name='Test Category')
		self.test_category.save_category()
		self.test_image = Image(
			name='Test image',
			description='test description',
			url='gallery/test.jpg',
			location=self.test_location
		)
		self.test_image.save_image()
		self.test_image.categories.add(self.test_category)

	def tearDown(self):
		Image.objects.all().delete()
		Category.objects.all().delete()
		Location.objects.all().delete()

	def test_get_images(self): self.assertTrue(len(Image.get_all()), 1)


class CategoryTestClass(TestCase):
	def setUp(self):
		self.test_category = Category(category_name='test category')
		self.test_category.save_category()

	def tearDown(self):
		Category.objects.all().delete()

	def test_get_categories(self):
		Category.objects.create(category_name='test category 2')
		self.assertTrue(len(Category.get_all()), 2)


class LocationTestClass(TestCase):
	def setUp(self):
		self.test_location = Location(location_name='test location')
		self.test_location.save_location()

	def tearDown(self):
		Location.objects.all().delete()

	def test_get_locations(self):
		Location.objects.create(location_name='test_location 2')
		self.assertTrue(len(Location.get_all()), 2)
