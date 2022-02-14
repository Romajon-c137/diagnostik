from django.shortcuts import render
from apps.slide.models import Slide

def main(request):
    slides = Slide.objects.filter(is_active=True).order_by('order')
    return render(request, 'main/index.html', {'slides': slides})



def services(request):
    return render(request, 'services/index.html')