from django.shortcuts import render
from django.http import HttpResponse,Http404    
from .models import Animais


def index (request):
    animals=Animais.objects.all()
    return render (request,'zoo.html',{'animal': animals})

def one_zoo(request,animal_id):
    try:
        animal=Animais.objects.get(pk=animal_id)
        return render(request,'one_zoo.html',{'aminal':animal})
    except Animais.DoesNotExist:
        raise Http404()