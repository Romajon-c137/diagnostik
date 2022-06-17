from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from weasyprint import HTML

from .forms import Form, ResultForm
from .models import Page, Lab


def conf(request):
    footer = Page.objects.filter(menu='footer', is_show=True, status='published').order_by('order')
    return {
        'form': Form(),
        'result_form': ResultForm(request.POST),
        'footer': footer
    }


def result(request):
    if request.method == 'POST':
        result_form = ResultForm(request.POST)
        if result_form.is_valid():
            try:
                result = Lab.objects.get(oder_number=result_form.data['oder_number'], pin=result_form.data['pin'])
                return render(request, 'result/index.html', {'result': result, 'result_form': result_form})
            except ObjectDoesNotExist:
                return render(request, 'result/index.html', {'notexist': "Нет такой записи", 'result_form': result_form})
    else:
        result_form = ResultForm()
    return render(request, 'result/index.html', {'result_form': result_form})


def html_to_pdf_view(request, oder_number, pin):
    result = Lab.objects.get(oder_number=oder_number, pin=pin)
    html_string = render_to_string('result/pdf_template.html', {'result': result})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/result.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('result.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="result.pdf"'
        return response