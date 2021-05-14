from rest_framework import serializers
#from django.contrib.auth.models import User
import posts.models as models

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = ["id", "title", "director", "actors", "genre", "release_date", "rating"]

"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
"""

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Email
        fields = ["from_who", "subject", "message", "to_whom", "date_sent"]
