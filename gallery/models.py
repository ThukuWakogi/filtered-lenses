from django.db import models

# Create your models here.


class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self): return f'{self.location_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self): return f'{self.category_name}'


class Image(models.Model):
    image_content = models.ImageField(upload_to='gallery/')
    name = models.CharField(max_length=30)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    def __str__(self): return f'{self.name}'
