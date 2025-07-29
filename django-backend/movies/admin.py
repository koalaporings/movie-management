from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date_added')
    search_fields = ('title',)

admin.site.register(Movie, MovieAdmin)
