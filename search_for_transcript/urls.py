from django.urls import path

from .views import HomePageView, SearchResultsView, CountView
# from . import views

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    # path('search/', ShowAllView.as_view(), name='search_results'),
    path('count/', CountView.as_view(), name='count'),
    # path('main/', views.main, name='main'),
    path('', HomePageView.as_view(), name='home')
]
