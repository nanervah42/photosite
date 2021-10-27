from django.urls import path
from .views import *

urlpatterns = [
    # path('', HomePhoto.as_view(), name='home'),
    path('', index, name='index'),
    ]