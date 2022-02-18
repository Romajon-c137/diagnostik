from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from weasyprint import HTML

from .forms import Form, ResultForm
from .models import Page, Lab


def conf(request):
    return {
        'form': Form()
    }


def footer_menu(request):
    footer = Page.objects.filter(menu='footer', is_show=True, status='published').order_by('order')
    return {'footer': footer}


def main(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            try:
                result = Lab.objects.get(oder_number=form.data['oder_number'], pin=form.data['pin'])
                return render(request, 'index.html', {'result': result, 'form': form})
            except ObjectDoesNotExist:
                return render(request, 'index.html', {'notexist': "Нет такой записи", 'form': form})
    else:
        form = ResultForm()
    return render(request, 'index.html', {'form': form})


def html_to_pdf_view(request, oder_number, pin):
    result = Lab.objects.get(oder_number=oder_number, pin=pin)
    html_string = render_to_string('pdf_template.html', {'result': result})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response