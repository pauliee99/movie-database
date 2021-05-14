from rest_framework import serializers
import posts.models as models

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = ["id", "title", "director", "actors", "genre", "release_date", "rating"]

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Email
        fields = ["from_who", "subject", "message", "to_whom", "date_sent"]
