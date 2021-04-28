from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

## Movie API Views ##

from posts.models import movie
from .serializers import movieSerializer

class MoviesListApiView(APIView):
    
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the movie items 
        '''
        
        movies = movie.objects
        serializer = movieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the movie with given movie data
        '''
        data = {
            'title': request.data.get('title'),
            'director': request.data.get('director'),
            'actors': request.data.get('actors'),
            'genre': request.data.get('genre'),
            'release_date': request.data.get('release_date'),
            'rating': request.data.get("rating")
        }
        serializer = movieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
