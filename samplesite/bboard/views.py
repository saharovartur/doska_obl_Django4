from django.http import HttpResponse

def index(request):
    return HttpResponse('Здесь будет находится список объявлений.')


