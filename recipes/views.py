from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    # a opção de status é apenas para estudo, não precisa usar
    # return render(request, 'recipes/home.html', status=201)
    # passar uma variavel
    return render(request, 'recipes/home.html', context={
        'name': 'Bruno Verdan',
    })


def contato(request):
    return HttpResponse('CONTATO')


def sobre(request):
    return HttpResponse('SOBRE')
