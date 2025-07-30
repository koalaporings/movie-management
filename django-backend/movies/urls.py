from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path("movie-list/", views.fetch_movie_list.as_view(), name="fetch_movie_list"),
    path("get-movie/", views.fetch_movie, name="fetch_movie"),
    path("create-movie/", views.create_movie, name="create_movie"),
    path("update-movie/", views.update_movie, name="update_movie"),
    path("delete-movie/", views.delete_movie, name="delete_movie")
]