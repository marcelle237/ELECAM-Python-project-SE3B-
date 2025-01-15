from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, welcome to the ELECAM web application!")
