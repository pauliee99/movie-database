from rest_framework import serializers
import posts.models as models

class movieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.movie
        fields = ["id", "title", "director", "actors", "genre", "release_date", "rating"]

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.user
        fields = ["id", "username", "email", "password", "date_registered"]

"""
Here, maybe its wrong to use inheritance through serializer classes
If something goes wrong, do exactly the same as the user serializer for the next 2 classes
"""

class viewerSerializer(userSerializer):
    class Meta:
        model = models.viewer
        fields = ["movies_viewed", "movies_rated", "movies_loved"]

class managerSerializer(userSerializer):
    class Meta:
        model = models.manager
        fields = ["movies_added"]

class emailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.email
        fields = ["from_who", "subject", "message", "to_whom", "date_sent"]
