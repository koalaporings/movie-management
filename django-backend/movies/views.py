from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Movie
from.serializers import MovieSerializer

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already taken'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create(
        username=username,
        password=make_password(password)  # hash the password
    )
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_movie(request):
    pk = request.GET.get("pk")
    if pk:
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


class fetch_movie_list(ListAPIView):
    queryset = Movie.objects.all().order_by('pk')
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
@permission_classes([IsAuthenticated])
def create_movie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        movie = serializer.save()
        return Response(MovieSerializer(movie).data, status=status.HTTP_201_CREATED)
    return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@parser_classes([MultiPartParser, FormParser])
@permission_classes([IsAuthenticated])
def update_movie(request):
    pk = request.GET.get("pk")
    if not pk:
        return Response({'error': 'No pk provided'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = MovieSerializer(movie, data=request.data, partial=True)
    if serializer.is_valid():
        updated_movie = serializer.save()
        return Response(MovieSerializer(updated_movie).data, status=status.HTTP_200_OK)
    return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_movie(request):
    pk = request.GET.get("pk")
    if not pk:
        return Response({"error": "No pk provided"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

    movie_title = movie.title
    movie.delete()
    return Response({"response": f"{movie_title} has been deleted"}, status=status.HTTP_200_OK)