from .views import *
from django.urls import path, include
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'user', ProfileViewSet, basename='profile')
router.register(r'country', CountryViewSet, basename='country')
router.register(r'director', DirectorViewSet, basename='directory')
router.register(r'actor', ActorViewSet, basename='actor')
router.register(r'genre', GenreViewSet, basename='genre')
router.register(r'movie', MovieListAPIView, basename='movie')
router.register(r'rating', RatingViewSet, basename='rating')



urlpatterns = [
    path('', include(router.urls)),
    path( 'movie/', MovieListAPIView.as_view({'get': 'list'}), name='movie-list' ),
    path( 'movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail' ),
]