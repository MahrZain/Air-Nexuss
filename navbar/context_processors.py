from .models import Header

def navbar(request):
    header = Header.objects.all()
    
    return {
        "header": header,
    }