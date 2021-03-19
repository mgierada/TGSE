from django.views.generic import TemplateView, ListView
from typing import Any, Dict, List
from django.utils.safestring import mark_safe
from django.db.models.query import QuerySet

from .models import Transcript


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Transcript
    template_name = 'search_results.html'
    context_object_name = 'episode_list'

    def get_queryset(self) -> QuerySet:
        ''' Get Transcript objects containing query in text filed

        Returns
        -------
        QuerySet
            transcript objects containing query in text filed

        '''
        self.query = self.request.GET.get('q')
        episode_list = Transcript.objects.filter(text__contains=self.query)
        return episode_list

    def get_context_data(
            self,
            **kwargs: Any) -> Dict[str, Any]:
        ''' Update context_data to be used in html

        Returns
        -------
        Dict[str, Any]
            updated context_data

        '''
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['count'] = self.count_total()
        episode_list = context['episode_list']
        transcripts_list = self.highlight()
        each_query_count = self.get_each_query_count().values()
        episodes_and_transcripts = zip(
            episode_list, each_query_count, transcripts_list)
        # context['count_each_query'] = self.count_each_query()
        context['ep_countq_trans'] = episodes_and_transcripts
        return context

    def highlight(self, **kwargs) -> List[str]:
        ''' Highlight query in transcript text

        Returns
        -------
        List[str]
            Formated transcript with html tags that displays hightlights while
            rendering

        '''
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        # query = self.request.GET.get('q')
        episode_list = context['episode_list']
        text_list = []
        for episode in episode_list:
            text = episode.text
            replacing_query = '<span class="highlighted"><strong>{}</strong></span>'.format(
                self.query)
            text = text.replace(self.query, replacing_query)
            text = mark_safe(text)
            text_list.append(text)
        return text_list

    def count_total(self) -> str:
        # ''' Count how many times query appears in database in total
        # (only text attribute)

        # Returns
        # -------
        # str
        #     text with info about how many query appears in database
        # '''
        # query = self.request.GET.get('q')
        # episode_list = Transcript.objects.filter(text__contains=query)
        # count = 0
        # for episode in episode_list:
        #     count += episode.text.count(query)
        each_query_count = self.get_each_query_count()
        total_count = sum(each_query_count.values())
        response = 'Found {} occurrences of "{}" in total'.format(
            total_count, self.query)
        return response

    def get_each_query_count(self):
        ''' Count how many times query appears in database in total
        (only text attribute)

        Returns
        -------
        str
            text with info about how many query appears in database

        '''
        # query = self.request.GET.get('q')
        episode_list = Transcript.objects.filter(text__contains=self.query)
        count = 0
        each_query_count = {}
        for episode in episode_list:
            count = episode.text.count(self.query)
            each_query_count[episode.episode_number] = count
        return each_query_count
