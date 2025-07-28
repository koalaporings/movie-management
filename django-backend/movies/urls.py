from django.urls import path
from . import views

urlpatterns = [
    path("movie-list/", views.fetch_movies, name="fetch_movie_list"),
    path("get-movie/<int:pk>/", views.fetch_movies, name="fetch_movie"),
    path("create-movie/", views.create_movie, name="create_movie"),
    path("update-movie/<int:pk>/", views.update_movie, name="update_movie"),
    path("delete-movie/<int:pk>/", views.delete_movie, name="delete_movie")
]