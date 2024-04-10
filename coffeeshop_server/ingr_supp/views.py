from django.shortcuts import render

from ingr_supp.models import Ingr,Supp

# Create your views here.
def view(request):
    supplies = Supp.objects.all()
    return render(request,'home.html',{'supplies':supplies})

def ingr(request):
    return render(request,'ingr.html')

def prod(request):
    return render(request,'prod.html')

def show_ingredients(request):
    ingredients = Ingr.objects.all()
    return render(request, 'ingr.html', {'ingredients': ingredients})

