from django.urls import path
from .views import *

urlpatterns = [
     path('', flames_view, name='flames'),
]
