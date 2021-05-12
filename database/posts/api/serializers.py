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
'''
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.user
        fields = ["id", "username", "email", "password", "date_registered"]
'''
"""
Here, maybe its wrong to use inheritance through serializer classes
If something goes wrong, do exactly the same as the user serializer for the next 2 classes
"""
"""
class viewerSerializer(UserSerializer):
    class Meta:
        model = models.viewer
        fields = ["movies_viewed", "movies_rated", "movies_loved"]

class managerSerializer(UserSerializer):
    class Meta:
        model = models.manager
        fields = ["movies_added"]
"""
class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Email
        fields = ["from_who", "subject", "message", "to_whom", "date_sent"]
