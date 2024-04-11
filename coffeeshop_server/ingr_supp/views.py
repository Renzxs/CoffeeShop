import json
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from .models import Ingr,Supp

# Create your views here.
def view(request):
    supplies = Supp.objects.all()
    return render(request,'home.html',{'supplies':supplies})

def prod(request):
    return render(request,'prod.html')

def ingr(request):
    ingredients = Ingr.objects.all()
    return render(request, 'ingredients.html', {'ingredients':ingredients})


from django.shortcuts import render, redirect
from .models import Ingr
from .forms import IngrForm, IngrFormUp

def add_ingredient(request):
    if request.method == 'POST':
        form = IngrForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingr')  # Redirect to the ingredients page after adding
    else:
        form = IngrForm()
    return render(request, 'ingredients.html', {'form': form})

from django.shortcuts import render, redirect
from django.http import HttpResponseServerError
from .forms import IngrFormUp
from .models import Ingr

def update_ingredient(request, ingredient_id):
    try:
        ingredient = Ingr.objects.get(pk=ingredient_id)
    except Ingr.DoesNotExist:
        return HttpResponseServerError("Ingredient not found")

    if request.method == 'POST':
        form = IngrFormUp(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingr')  # Redirect to the ingredients page after updating
        else:
            # Redirect to error.html if form is invalid
            return render(request, 'error.html', {'form': form})
    else:
        form = IngrFormUp(instance=ingredient)
    
    return render(request, 'ingredients.html', {'form': form, 'ingredient_id': ingredient_id})

def delete_ingredient(request, ingredient_id):
    # Retrieve the ingredient object from the database
    ingredient = get_object_or_404(Ingr, pk=ingredient_id)
    
    if request.method == 'POST':
        # Delete the ingredient from the database
        ingredient.delete()
        return redirect('ingr')  # Redirect to the ingredients page after deletion
    
    # If the request method is not POST, render a confirmation page
    return render(request, 'confirm_delete.html', {'ingredient': ingredient})