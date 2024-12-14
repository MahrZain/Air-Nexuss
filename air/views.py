from django.shortcuts import render
from navbar.models import Header

def home(request):
    return render(request , 'index.html')

def header(request):
    header = Header.objects.all()

    data = {
        "header": header,
    }
    return render(request, "header.html", data)