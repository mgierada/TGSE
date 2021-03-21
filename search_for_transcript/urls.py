from django.urls import path

from .views import HomePageView, SearchResultsView, TranscriptView
# from . import views

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    # path('main/', views.main, name='main'),
    path('', HomePageView.as_view(), name='home'),
    path('search/transcript/<int:episode_number>/<str:query>',
         TranscriptView.as_view(), name='transcript')
]
