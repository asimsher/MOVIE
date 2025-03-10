from django.shortcuts import render
from rest_framework import viewsets
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

class ProfileDetailViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, MethodCheck]


class CountryViewSet( viewsets.ModelViewSet ):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer



class DirectorViewSet( viewsets.ModelViewSet ):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class ActorViewSet( viewsets.ModelViewSet ):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet( viewsets.ModelViewSet ):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilters
    search_fields = ['movie_name']
    ordering_fields = ['year']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MovieLanguagesViewSet( viewsets.ModelViewSet ):
    queryset = MovieLanguages.objects.all()
    serializer_class = MovieLanguagesSerializer


class MomentsViewSet( viewsets.ModelViewSet ):
    queryset = Moments.objects.all()
    serializer_class = MomentsSerializer


class RatingViewSet( viewsets.ModelViewSet ):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class FavoriteViewSet( viewsets.ModelViewSet ):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer



class FavoriteMovieViewSet( viewsets.ModelViewSet ):
    queryset = FavoriteMovie.objects.all()
    serializer_class = FavoriteMovieSerializer


class HistoryViewSet( viewsets.ModelViewSet ):
    queryset = History.objects.all()
    serializer_class = HistorySerializer



