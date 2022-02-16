from .forms import Form
from .models import Page


def conf(request):
    return {
        'form': Form()
    }


def footer_menu(request):
    footer = Page.objects.filter(menu='footer', is_show=True, status='published').order_by('order')
    return {'footer': footer}