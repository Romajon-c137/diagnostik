from json.tool import main
from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main/main.html')