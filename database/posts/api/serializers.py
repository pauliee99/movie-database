from rest_framework import serializers
import posts.models

class movieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.movie
        fields = ["id", "title", "director", "actors", "genre", "release_date", "rating"]

#... and the rest entity serializers
# after we will create API views
