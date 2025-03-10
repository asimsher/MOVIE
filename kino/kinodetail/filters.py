from django_filters.rest_framework import FilterSet
from .models import Movie


class MovieFilters(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'country': ['gte', 'lte'],
            'year': ['gte', 'lte'],
            'genre': ['gte', 'lte'],
            'status_movie':  ['gte', 'lte'],
            'actor':  ['gte', 'lte'],
            'director':  ['gte', 'lte']
        }