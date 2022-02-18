from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('page/<str:slug>/', page, name='page'),
    path('form/', form, name='accept'),
    path('labs', labs, name='labs'),
    path('news', news, name='news'),
    path('prices', prices, name='prices'),
    path('clinic', clinic, name='clinic'),
    path('specialists', specialists, name='specialists'),
    path('services', services, name='services'),
]