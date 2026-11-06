from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Lucy, my first Django app works!")