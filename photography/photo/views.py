from django.shortcuts import render
from django.views.generic import TemplateView


class HomePhoto(TemplateView):
    template_name = 'photo/index.html'
    context_object_name = 'photo'
    title = 'test'

    def get_context_data(self, *, object_list=None, **kwargs):  # ...для динамичных данных
        context = super().get_context_data(**kwargs)            # получаем контекст, который уже есть
        context['title'] = 'Главная страница'                   # дополняем его
        return context