from typing import List
from django.views.generic import TemplateView, ListView


from .models import City


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = City
    template_name = 'search_results.html'
