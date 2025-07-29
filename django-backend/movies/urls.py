from django.urls import path
from . import views

urlpatterns = [
    path("movie-list/", views.fetch_movies, name="fetch_movie_list"),
    path("get-movie/", views.fetch_movies, name="fetch_movie"),
    path("create-movie/", views.create_movie, name="create_movie"),
    path("update-movie/", views.update_movie, name="update_movie"),
    path("delete-movie/", views.delete_movie, name="delete_movie")
]