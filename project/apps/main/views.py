from django.shortcuts import render
from apps.slide.models import Slide

def main(request):
    slides = Slide.objects.filter(is_active=True).order_by('order')
    return render(request, 'main/index.html', {'slides': slides})



def services(request):
    return render(request, 'services/index.html')

def labs(request):
    return render(request, 'labs/index.html')

def news(request):
    return render(request, 'news/index.html')

def prices(request):
    return render(request, 'prices/index.html')

def reviews(request):
    return render(request, 'reviews/index.html')

def specialists(request):
    return render(request, 'specialists/index.html')