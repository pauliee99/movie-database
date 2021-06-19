from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

## Movie API Views ##

from posts.models import Movie
from .serializers import MovieSerializer

class MoviesListApiView(APIView):

    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the movie items
        '''

        movies = Movie.objects
        serializer = MovieSerializer(movies, many=True)
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
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MoviesDetailApiView(APIView):

    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, movie_id):
        '''
        Helper method to get the object with given movie_id
        '''
        try:
            return Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
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

        serializer = MovieSerializer(movie_instance)
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
        serializer = MovieSerializer(instance = movie_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # extra method to use it on deletion
    def inform_all_id(self):
        id = 1
        while True:
            movie = self.get_object(id)
            if not movie:
                return
            data = {
                'id': id,
                'title': movie.title,
                'director': movie.director,
                'actors': movie.actors,
                'genre': movie.genre,
                'release_date': movie.release_date,
                'rating': movie.rating
            }
            serializer = MovieSerializer(instance = movie, data=data, partial = True)
            if serializer.is_valid():
                serializer.save()

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
        Movie.objects.get(id=movie_id).delete()
        del movie_instance
        self.inform_all_id()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

## Email API Views ##

from posts.models import Email
from .serializers import EmailSerializer

class EmailListApiView(APIView):

    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the email items
        '''
        emails = Email.objects
        serializer = EmailSerializer(emails, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the email with given email data
        '''
        data = {
            'from_who': request.data.get('from_who'),
            'subject': request.data.get('subject'),
            'message': request.data.get('message'),
            'to_whom': request.data.get('to_whom'),
            'date_sent': request.data.get('date_sent')
        }
        serializer = EmailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmailDetailApiView(APIView):

    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, email_id):
        '''
        Helper method to get the object with given email_id
        '''
        try:
            return Email.objects.get(id=email_id)
        except Email.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, email_id, *args, **kwargs):
        '''
        Retrieves the email with given email_id
        '''
        email_instance = self.get_object(email_id)
        if not email_instance:
            return Response(
                {"res": "Object with email id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = EmailSerializer(email_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, email_id, *args, **kwargs):
        '''
        Updates the email item with given email_id if exists
        '''
        email_instance = self.get_object(email_id)
        if not email_instance:
            return Response(
                {"res": "Object with email id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'from_who': request.data.get('from_who'),
            'subject': request.data.get('subject'),
            'message': request.data.get('message'),
            'to_whom': request.data.get('to_whom'),
            'date_sent': request.data.get('date_sent')
        }
        serializer = EmailSerializer(instance = email_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, email_id, *args, **kwargs):
        '''
        Deletes the email item with given email_id if exists
        '''
        email_instance = self.get_object(email_id)
        if not email_instance:
            return Response(
                {"res": "Object with email id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        email_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
