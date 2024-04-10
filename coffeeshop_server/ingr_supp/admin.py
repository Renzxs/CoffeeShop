from django.contrib import admin
from .models import Ingr,Supp

@admin.register(Ingr)
class IngrAdmin(admin.ModelAdmin):
    list_display = ('ingr_name', 'ingr_quant', 'ingr_desc', 'ingr_catg', 'ingr_cost', 'ingr_suppNo', 'ingr_exp', 'ingr_batch', 'ingr_date', 'ingr_act')

@admin.register(Supp)
class SuppAdmin(admin.ModelAdmin):
    list_display = ('Supp_name', 'Supp_quant', 'Supp_desc', 'Supp_catg', 'Supp_cost', 'Supp_suppNo', 'Supp_exp', 'Supp_batch', 'Supp_date', 'Supp_act')
