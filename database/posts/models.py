from django.db import models

# Create your models here.
class movies(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=60)
    actos = models.TextField(max_length=512)
    genre = models.CharField(max_length=40)
    release_date = models.DateField()
    rating = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'movies'

class users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    password = models.TextField(max_length=512)
    date_registered = models.DateField()

    class Meta:
        verbose_name_plural = 'users'