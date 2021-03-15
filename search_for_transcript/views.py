from django.http.response import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views import View
from typing import Any, Dict

from .models import Transcript


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Transcript
    template_name = 'search_results.html'
    context_object_name = 'episode_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        episode_list = Transcript.objects.filter(text__contains=query)
        return episode_list

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['count'] = self.count()
        return context

    def count(self):
        query = self.request.GET.get('q')
        # query = 'SGU'
        episode_list = Transcript.objects.filter(text__contains=query)
        count = 0
        for episode in episode_list:
            count += episode.text.count(query)
        response = 'Found {} occurrences of "{}" in DB'.format(count, query)
        return response
