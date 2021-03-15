from typing import List
from django.views.generic import TemplateView, ListView
from django.db.models import Q


from .models import Transcript


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Transcript
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Transcript.objects.filter(text__contains=query)
        return object_list
