from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import People


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    person = People.objects.all()
    return render(request, "index.html", {'result': obj, 'result2': person})


