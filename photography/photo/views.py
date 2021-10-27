from django.shortcuts import render
from django.views.generic import TemplateView


class HomePhoto(TemplateView):
    template_name = 'photo/index.html'
    context_object_name = 'photo'


def index(request):
    context = {
        'title': 'test'
    }
    return render(request, 'photo/index.html', context)