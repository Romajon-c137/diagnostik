from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .serializers import *
from apps.main.models import Lab, Result


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ResultViewSet(ModelViewSet):
    
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class LabViewSet(ModelViewSet):
    
    queryset = Lab.objects.all()
    serializer_class = LabSerializer
    # pagination_class = StandardResultsSetPagination