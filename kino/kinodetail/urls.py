from .views import *
from django.urls import path, include

urlpatterns = [
    path('user/', ProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('user/<int:pk>/', ProfileDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                       'delete': 'destroy'}), name='user-detail'),

    path('country/', CountryViewSet.as_view({'get': 'list', 'post': 'create'}), name='country-list'),
    path('country/<int:pk>/', CountryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy'}), name='country-detail'),

    path('director/', DirectorViewSet.as_view({'get': 'list', 'post': 'create'}), name='director-list'),
    path('director/<int:pk>/', DirectorViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                     'delete': 'destroy'}), name='director-detail'),

    path('actor/', ActorViewSet.as_view({'get': 'list', 'post': 'create'}), name='actor-list'),
    path('actor/<int:pk>/', ActorViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy'}), name='actor-detail'),

    path('genre/', GenreViewSet.as_view({'get': 'list', 'post': 'create'}), name='genre-list'),
    path('genre/<int:pk>/', GenreViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                       'delete': 'destroy'}), name='genre-detail'),

    path('movie/', MovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie-list'),
    path('movie/<int:pk>/', MovieViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy'}), name='movie-detail'),

    path('movie_lang/', MovieLanguagesViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_lang-list'),
    path('movie_lang/<int:pk>/', MovieLanguagesViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                     'delete': 'destroy'}), name='movie_lang-detail'),

    path('moments/', MomentsViewSet.as_view({'get': 'list', 'post': 'create'}), name='moments-list'),
    path('moments/<int:pk>/', MomentsViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy'}), name='moments-detail'),

    path('rating/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating-list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                       'delete': 'destroy'}), name='rating-detail'),

    path('favorite/', FavoriteViewSet.as_view({'get': 'list', 'post': 'create'}), name='favorite-list'),
    path('favorite/<int:pk>/', FavoriteViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy'}), name='favorite-detail'),

    path('favorite_mov/', FavoriteMovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='favorite_mov-list'),
    path('favorite_mov/<int:pk>/', FavoriteMovieViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                     'delete': 'destroy'}), name='favorite_mov-detail'),

    path('history/', HistoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='history-list'),
    path('history/<int:pk>/', HistoryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy'}), name='history-detail'),

]

