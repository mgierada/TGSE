from django.http.response import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views import View
from typing import Any, Dict
from django.utils.safestring import mark_safe
# from haystack.utils.highlighting import Highlighter
from haystack.utils import Highlighter

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
        # entries = Transcript.objects.all()
        # en0 = entries[0]
        # text = en0.text
        # # self.highlight_search(text, query)
        return episode_list

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['count'] = self.count()
        # context['text'] = self.highlight()
        episode_list = context['episode_list']
        transcript = self.highlight()
        together = zip(episode_list, transcript)
        context['together'] = together
        return context

    def highlight(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        query = self.request.GET.get('q')
        episode_list = context['episode_list']
        text_list = []
        for episode in episode_list:
            text = episode.text
            replacing_query = '<span class="highlighted">{}</span>'.format(
                query)
            text = text.replace(query, replacing_query)
            text = mark_safe(text)
            text_list.append(text)
        # print(text_list)
        return text_list

        # highlighter = self.highlight_search(text, query)
        # high_li = highlighter.highlight(entries[0].text)
        # context['high_li'] = high_li
        # print(high_li)
        # context['color'] = self.highlight_search(text, query)

    # def highlight_search(self, text, query):
    #     print('runing this')
    #     highlight = Highlighter(query)
    #     # print(highlight,highlight([0].text))
    #     return highlight

    def count(self):
        query = self.request.GET.get('q')
        # query = 'SGU'
        episode_list = Transcript.objects.filter(text__contains=query)
        count = 0
        for episode in episode_list:
            count += episode.text.count(query)
        # response = HttpResponse()
        # response['count'] = count
        response = 'Found {} occurrences of "{}" in DB'.format(count, query)
        # return HttpResponse(response)
        return response


class CountView(View):
    model = Transcript
    template_name = 'search_results.html'

    def get(self, request, *args, **kwargs):
        # query = self.request.GET.get('q')
        query = 'SGU'
        episode_list = Transcript.objects.filter(text__contains=query)
        count = 0
        for episode in episode_list:
            count += episode.text.count(query)
        response = HttpResponse()
        response['count'] = count
        response = 'Found {} occurrences of "{}" in DB'.format(count, query)
        return HttpResponse(response)

    def get_queryset(self):
        query = self.request.GET.get('q')
        episode_list = Transcript.objects.filter(text__contains=query)
        count = 0
        for episode in episode_list:
            count += episode.text.count(self.query)
        response = HttpResponse()
        response['count'] = count
        # contex = {'count': count}
        return response

# def main(request):
#     fun1 = index(request)
#     fun2 = detail(request)
#     response = fun1 + fun2
#     return response


# def index(request):
#     return HttpResponse("You're looking at question")


# def detail(request):
#     return HttpResponse('hahaha')
