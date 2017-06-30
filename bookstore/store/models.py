from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

def image_upload_path(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return "{0}, {1}".format(self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    cover = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    publish_date = models.DateField(default=timezone.now)
    text = models.TextField()