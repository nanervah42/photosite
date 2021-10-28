from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePhoto.as_view(), name='home'),
    path('price/', Price.as_view(), name='price'),
    path('collection/', Collection.as_view(), name='collection'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('about/', About.as_view(), name='about'),
    ]