
from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .view import ResultViewSet, LabViewSet

router = routers.DefaultRouter()
router.register('results', ResultViewSet, 'results')
router.register('labs', LabViewSet, 'labs')

urlpatterns = [
    path("", include(router.urls), name='api'),
]