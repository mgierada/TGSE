from django.urls import path

from .views import (HomePageView,
                    SearchResultsView,
                    TranscriptHighlightView,
                    TranscriptReadModeView,
                    APIGetAllEpisodes,
                    APIGetEpisode)

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    # path('main/', views.main, name='main'),
    path('', HomePageView.as_view(), name='home'),
    path('search/transcript_highlight/<int:episode_number>/<str:query>',
         TranscriptHighlightView.as_view(), name='transcript'),
    path('search/transcript_read_mode/<int:episode_number>/<str:query>',
         TranscriptReadModeView.as_view(), name='transcript_plain'),
    path('episodes/', APIGetAllEpisodes.as_view(), name='api_list'),
    path('episodes/<int:episode_number>/',
         APIGetEpisode.as_view(), name='api_list_episode')
]
