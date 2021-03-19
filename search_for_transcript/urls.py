from django.urls import path

from .views import HomePageView, SearchResultsView, TranscriptView
# from . import views

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    # path('main/', views.main, name='main'),
    path('', HomePageView.as_view(), name='home'),
    # path('transcript/episode<int:episode_number>',
    #      TranscriptView.as_view(), name='transcript')
    path('search_for_transcript/transcript/<int:episode_number>/',
         TranscriptView.as_view(), name='transcript')
]
