from django.shortcuts import render
from rest_framework import viewsets, generics, status
from .serializers import *
from .filters import MovieFilters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import permissions
from .permissions import MethodCheck

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, MethodCheck]


class CountryViewSet( viewsets.ModelViewSet ):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, MethodCheck]

class DirectorViewSet( viewsets.ModelViewSet ):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, MethodCheck]

class ActorViewSet( viewsets.ModelViewSet ):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, MethodCheck]

class GenreViewSet( viewsets.ModelViewSet ):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, MethodCheck]

class MovieListAPIView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilters
    search_fields = ['movie_name']
    ordering_fields = ['year']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, MethodCheck]

class MovieLanguagesViewSet( viewsets.ModelViewSet ):
    queryset = MovieLanguages.objects.all()
    serializer_class = MovieLanguagesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, MethodCheck]

class MomentsViewSet( viewsets.ModelViewSet ):
    queryset = Moments.objects.all()
    serializer_class = MomentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, MethodCheck]

class RatingViewSet( viewsets.ModelViewSet ):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, MethodCheck]

class FavoriteViewSet( viewsets.ModelViewSet ):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, MethodCheck]


class FavoriteMovieViewSet( viewsets.ModelViewSet ):
    queryset = FavoriteMovie.objects.all()
    serializer_class = FavoriteMovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, MethodCheck]

class HistoryViewSet( viewsets.ModelViewSet ):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, MethodCheck]


