from email.policy import default
from django.db import models
from django.forms import SlugField
from django.urls import reverse



class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    department = models.CharField(max_length=255)


class Contact(models.Model):
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=166)
    street = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    coutry = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2 ,null=False)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    image = models.ImageField(default='null', upload_to = './main/static/imgs')
    file = models.FileField(default='null', upload_to='./main/static/files')
    video = models.FileField(default='null', upload_to='./main/static/videos')

    def url_correction(self):
        url = str(self.image)
        return url[4:]

    def file_url_correction(self):
        url = str(self.file)
        return url[4:]

    def video_url_correction(self):
        url = str(self.video)
        return url[4:]

    def get_absolute_url(self):
        return reverse('main:product_view', kwargs={'slug': self.slug})
