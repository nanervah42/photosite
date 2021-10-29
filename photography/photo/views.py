from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Carousel

class HomePhoto(ListView):
    model = Carousel
    template_name = 'photo/index.html'
    context_object_name = 'carousel'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['home_under_line'] = 'class="colorlib-active"'
        return context

    def get_queryset(self):
        return Carousel.objects.filter(is_published=True)

class Price(TemplateView):
    template_name = 'photo/price.html'
    context_object_name = 'price'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Услуги и цены'
        context['price_under_line'] = 'class="colorlib-active"'
        return context

class Collection(TemplateView):
    template_name = 'photo/collection.html'
    context_object_name = 'collection'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Работы'
        context['collection_under_line'] = 'class="colorlib-active"'
        return context

class Contacts(TemplateView):
    template_name = 'photo/contacts.html'
    context_object_name = 'сontacts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        context['contacts_under_line'] = 'class="colorlib-active"'
        return context

class About(TemplateView):
    template_name = 'photo/about.html'
    context_object_name = 'about'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обо мне'
        context['about_under_line'] = 'class="colorlib-active"'
        return context
