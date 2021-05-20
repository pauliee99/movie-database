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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["id", "password", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined", "is_viewer", "is_manager"]

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manager
        fields = ["user_id"]

class ViewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Viewer
        fields = ["user_id"]
