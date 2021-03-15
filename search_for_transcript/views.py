from typing import List
from django.views.generic import TemplateView, ListView
from django.db.models import Q


from .models import City, Transcript


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Transcript
    template_name = 'search_results.html'

    def get_queryset(self):
        result = super(SearchResultsView, self).get_queryset()
        query = self.request.GET.get('q')
        object_list = Transcript.objects.filter(Q(text__contains=query))
        return object_list
        # if query:
        #     postresult = Transcript.objects.filter(text__contains=query)
        #     result = postresult
        # else:
        #     result = None
        # return result
