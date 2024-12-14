from django.shortcuts import render
from navbar.models import Header
from contact.models import Contact
from django.contrib import messages
def home(request):
    return render(request , 'index.html')
def contact(request):
    if request == 'GET':
        return render(request , 'contact.html')
def contact_save(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        if not name or not email or not message:
            messages.error(request, 'Please Fill All The fields')
        else:
            con = Contact(name=name,email=email,message=message)
            messages.success(request, 'Sent Successful')
            con.save()
            

def header(request):
    header = Header.objects.all()

    data = {
        "header": header,
    }
    return render(request, "header.html", data)