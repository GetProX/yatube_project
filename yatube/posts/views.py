from django.http import HttpResponse


def index(request):
    return HttpResponse('Главаня старница')


def group_posts(request, pk):
    return HttpResponse(f'Номер группы {pk}')