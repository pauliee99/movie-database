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

class MoviesDetailApiView(APIView):

    def get_object(self, movie_id):
        '''
        Helper method to get the object with given movie_id
        '''
        try:
            return movie.objects.get(id=movie_id)
        except movie.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, movie_id, *args, **kwargs):
        '''
        Retrieves the movie with given movie_id
        '''
        movie_instance = self.get_object(movie_id)
        if not movie_instance:
            return Response(
                {"res": "Object with movie id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = movieSerializer(movie_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, movie_id, *args, **kwargs):
        '''
        Updates the movie item with given movie_id if exists
        '''
        movie_instance = self.get_object(movie_id)
        if not movie_instance:
            return Response(
                {"res": "Object with movie id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'),
            'director': request.data.get('director'),
            'actors': request.data.get('actors'),
            'genre': request.data.get('genre'),
            'release_date': request.data.get('release_date'),
            'rating': request.data.get("rating")
        }
        serializer = movieSerializer(instance = movie_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, movie_id, *args, **kwargs):
        '''
        Deletes the movie item with given movie_id if exists
        '''
        movie_instance = self.get_object(movie_id)
        if not movie_instance:
            return Response(
                {"res": "Object with movie id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
                                                                                                                        )
        movie_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

## More API Views soon... ##

