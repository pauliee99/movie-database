from django.db import models

# Create your models here.
class movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=60)
    actors = models.TextField(max_length=512)
    genre = models.CharField(max_length=40)
    release_date = models.DateField()
    rating = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'movies'

class user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    password = models.TextField(max_length=512)
    date_registered = models.DateTimeField('date registered')

    class Meta:
        verbose_name_plural = 'users'

class viewer(user):
    movies_viewed = models.BigIntegerField()
    movies_rated = models.BigIntegerField()
    movies_loved = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'viewers'

class manager(user):
    movies_added = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'managers'
