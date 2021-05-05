from django.db import models

# Create your models here.
class movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=60)
    actors = models.TextField(max_length=512)
    genre = models.CharField(max_length=40)
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        verbose_name_plural = 'movies'

    def __str__(self):
        return self.title

class user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    password = models.TextField(max_length=512)
    date_registered = models.DateTimeField('date registered')

    class Meta:
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username

class viewer(user):
    movies_viewed = models.BigIntegerField()
    movies_rated = models.BigIntegerField()
    movies_loved = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'viewers'

    def __str__(self):
        return self.movies_viewed

class manager(user):
    movies_added = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'managers'

    def __str__(self):
        return self.movies_added

class email(models.Model):
    id = models.AutoField(primary_key=True)
    from_who = models.CharField(max_length=60)
    subject = models.TextField(max_length=200)
    message = models.TextField(max_length=1024)
    to_whom = models.CharField(max_length=60)
    date_sent = models.DateTimeField('date sent')

    class Meta:
        verbose_name_plural = 'emails'

    def __str__(self):
        return self.message
