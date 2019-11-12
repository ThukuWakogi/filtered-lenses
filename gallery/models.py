from django.db import models

# Create your models here.


class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def save_location(self): self.save()
    
    @classmethod
    def get_all(cls): return cls.objects.all()


    def __str__(self): return f'{self.location_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    @classmethod
    def get_all(cls): return cls.objects.all()

    def __str__(self): return f'{self.category_name}'


class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    url = models.ImageField(upload_to='gallery/', max_length=500)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    def save_image(self): self.save()

    @classmethod
    def get_all(cls): return cls.objects.all()

    @classmethod
    def by_categories_and_location(cls, _location, _category):
        return cls.objects.filter(categories__in=[_category], location=_location)

    @classmethod
    def by_category(cls, _category):
        return cls.objects.filter(categories__in=[_category])

    @classmethod
    def by_location(cls, _location):
        return cls.objects.filter(location=_location)
    
    @classmethod
    def search_image(cls, _search_term):
        return cls.objects.filter(name__contains= _search_term)

    def __str__(self): return f'{self.name}'
