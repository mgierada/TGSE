from django.urls import path

from .views import (HomePageView,
                    SearchResultsView,
                    TranscriptView,
                    TranscriptPlainView,
                    APIGetAllEpisodes,
                    APIGetEpisode)

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    # path('main/', views.main, name='main'),
    path('', HomePageView.as_view(), name='home'),
    path('search/transcript/<int:episode_number>/<str:query>',
         TranscriptView.as_view(), name='transcript'),
    path('search/transcript_plain/<int:episode_number>/<str:query>',
         TranscriptPlainView.as_view(), name='transcript_plain'),
    path('episodes/', APIGetAllEpisodes.as_view(), name='api_list'),
    path('episodes/<int:episode_number>/',
         APIGetEpisode.as_view(), name='api_list_episode')
]
