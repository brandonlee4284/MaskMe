from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class AboutUs(models.Model):
    paragraph = models.CharField(max_length=10000)
    topic = models.CharField(max_length=10000)
    image_url = models.CharField(max_length=10000)


class Customize(models.Model):
    message = models.CharField(max_length=10000)
    other = models.CharField(max_length=10000)

class Home(models.Model):
    message = models.CharField(max_length=10000)
    video_url = models.CharField(max_length=10000)

class ConfirmationPage(models.Model):
    message = models.CharField(max_length=10000)
    other = models.CharField(max_length=10000)

class Promo(models.Model):
    message = models.CharField(max_length=10000)
    other = models.CharField(max_length=10000)

class Test(models.Model):
    message = models.CharField(max_length=10000)
    other = models.CharField(max_length=10000)


class Payment(models.Model):
    message = models.CharField(max_length=10000)
    other = models.CharField(max_length=10000)


class Customize1(models.Model):
    message = models.CharField(max_length=10000)
    other = models.CharField(max_length=10000)

class Customize2(models.Model):
    message = models.CharField(max_length=10000)
    other = models.CharField(max_length=10000)

class Customize3(models.Model):
    message = models.CharField(max_length=10000)
    other = models.CharField(max_length=10000)


