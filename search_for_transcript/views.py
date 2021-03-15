from django.views.generic import TemplateView, ListView
from django.shortcuts import render

from .models import Transcript


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Transcript
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        episode_list = Transcript.objects.filter(text__contains=query)
        contex = {'episode_list': episode_list}
        # return render(request, 'search_results.html', contex)
        return episode_list

    def count_occurences(self):
        episode_list = self.get_queryset()
        count = 0
        for episode in episode_list:
            count += episode.text.count(self.query)
        print(count)
        return count
