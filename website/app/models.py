from django.db import models
from django.db.models.fields.files import ImageField
from django.db.models import ForeignKey


# Create your models here.
class Brand(models.Model):
    name = models.CharField(blank=False, max_length=50, primary_key=True)
    enabled = models.BooleanField()

    def __str__(self):
        return f"{self.name}, {self.enabled}"


class Bodywood(models.Model):
    name = models.CharField(blank=False, max_length=50)
    enabled = models.BooleanField()

    def __str__(self):
        return f"{self.name}, {self.enabled}"


class Neckwood(models.Model):
    name = models.CharField(blank=False, max_length=50)
    enabled = models.BooleanField()

    def __str__(self):
        return f"{self.name}, {self.enabled}"


class Pickups(models.Model):
    name = models.CharField(blank=False, max_length=50)
    enabled = models.BooleanField()

    def __str__(self):
        return f"{self.name}, {self.enabled}"


class Color(models.Model):
    name = models.CharField(blank=False, max_length=50, primary_key=True)
    enabled = models.BooleanField()

    def __str__(self):
        return f"{self.name}, {self.enabled}"


class GuitarPic(models.Model):
    pic = models.ImageField(upload_to='uploads')
    brand = ForeignKey('Brand', on_delete=models.DO_NOTHING)
    color = ForeignKey('Color', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.brand.name} {self.color.name}: {self.pic}"


class Order(models.Model):
    pic_id = models.IntegerField()
    brand = models.CharField(blank=False, max_length=50)
    bw = models.CharField(blank=False, max_length=50)
    nw = models.CharField(blank=False, max_length=50)
    pickups = models.CharField(blank=False, max_length=50)
    color = models.CharField(blank=False, max_length=50)

    name = models.CharField(blank=False, max_length=50)
    tel = models.CharField(blank=False, max_length=50)
    notes = models.TextField(blank=True)
    date = models.DateTimeField(blank=True)

    def __str__(self):
        return f"{self.name}: {self.color} {self.brand} with {self.bw} body, {self.nw} neck, {self.pickups} pickups"
