from django.db import models

class Movie(models.Model):
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

class Email(models.Model):
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
