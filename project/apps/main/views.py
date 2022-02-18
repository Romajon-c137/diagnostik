from unicodedata import category
from django.shortcuts import render
from django.contrib import messages

from apps.slide.models import Slide
from apps.services.models import Service, Category as ServiceCategory
from apps.specialists.models import Department, Person, Role
from .models import FreeCall, Page
from .forms import Form

def main(request):
    doctors = Person.objects.filter(published=True, role=2)
    slides = Slide.objects.filter(is_active=True).order_by('order')
    return render(request, 'main/index.html', {'slides': slides, 'doctors': doctors})



def services(request):
    services = Service.objects.filter(category__slug=request.GET['category']) if 'category' in request.GET else Service.objects.all()
    serviceCategory = ServiceCategory.objects.filter(is_active=True)
    active = request.GET['category'] if 'category' in request.GET else 'all'
    return render(request, 'services/index.html', {'services': services.filter(published=True, category__is_active=True), 'serviceCategory': serviceCategory, 'active': active})

def labs(request):
    return render(request, 'labs/index.html')

def news(request):
    return render(request, 'news/index.html')

def prices(request):
    return render(request, 'prices/index.html')

def clinic(request):
    return render(request, 'clinic/index.html')

def specialists(request):
    roles = Role.objects.filter(published=True)
    departments = Department.objects.filter(published=True)
    person = Person.objects.filter(published=True)
    return render(request, 'specialists/index.html', {'roles': roles, 'departments': departments, 'person': person})

def form(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if FreeCall.objects.filter(e_mail=instance.e_mail).exists():
                messages.warning(request, "Your Email Already exists in our database")
            else:
                instance.save()
                messages.success(request, "Your Email has been submitted to our database")
            return render(request, 'components/free_call.html', {'form': form})
    else:
        form = Form()
        return render(request, "components/free_call.html", {'form': form})

def page(request, slug):
    page = Page.objects.get(slug=slug)
    return render(request, 'main/page.html', {'page': page})