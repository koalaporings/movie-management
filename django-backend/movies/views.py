from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .forms import MovieForm
from .models import Movie
from.serializers import MovieSerializer

# Create your views here.
@api_view(['GET'])
def fetch_movies(request):
    pk = request.GET.get("pk")
    if pk:
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=404)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movies = Movie.objects.all().order_by('pk')
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def create_movie(request):
    form = MovieForm(request.POST, request.FILES)
    if form.is_valid():
        movie = form.save()
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data, status=201)
    else:
        return JsonResponse({"errors": form.errors}, status=400)


@csrf_exempt
@api_view(['PUT'])
def update_movie(request):
    pk = request.GET.get("pk")
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return JsonResponse({'error': 'Movie not found'}, status=404)

    form = MovieForm(request.POST, request.FILES, instance=movie)
    for field in list(form.fields):
        if field not in request.POST and field not in request.FILES:
            form.fields.pop(field)
    if form.is_valid():
        updated_movie = form.save()
        serializer = MovieSerializer(updated_movie)
        return JsonResponse(serializer.data, status=200)
    else:
        return JsonResponse({'errors': form.errors}, status=400)


@csrf_exempt
@api_view(['DELETE'])
def delete_movie(request):
    pk = request.GET.get("pk")
    if pk:
        try:
            movie = Movie.objects.get(pk=pk)
            movie_deletion_message = f"{movie.title} has been deleted"
            movie.delete()
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=404)
        return JsonResponse({"response": movie_deletion_message})