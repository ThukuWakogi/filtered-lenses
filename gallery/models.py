from django.db import models

# Create your models here.


class Location(models.Model):
    location_name = models.CharField(max_length=30)


class Category(models.Model):
    Category_name = models.CharField(max_length=30)


class Image(models.Model):
    image_content = models.ImageField(upload_to='gallery/')
    name = models.CharField(max_length=30)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
