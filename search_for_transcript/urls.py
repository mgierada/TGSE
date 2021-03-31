from django.urls import path

from .views import (APIViewListEpisode, HomePageView,
                    SearchResultsView,
                    TranscriptView,
                    TranscriptPlainView,
                    APIViewList,
                    APIViewListEpisode)

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    # path('main/', views.main, name='main'),
    path('', HomePageView.as_view(), name='home'),
    path('search/transcript/<int:episode_number>/<str:query>',
         TranscriptView.as_view(), name='transcript'),
    path('search/transcript_plain/<int:episode_number>/<str:query>',
         TranscriptPlainView.as_view(), name='transcript_plain'),
    path('api_list/', APIViewList.as_view(), name='api_list'),
    path('api_list/<int:episode_number>/',
         APIViewListEpisode.as_view(), name='api_list_episode')
]
