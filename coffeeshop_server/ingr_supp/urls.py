from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('stocks',views.view, name="view"),
    path('ingr',views.ingr, name = "ingr"),
    path('products',views.prod, name="prod"),
    path('add_ingredient/', views.add_ingredient, name='add_ingredient'),
    path('update_ingredient/<int:ingredient_id>/', views.update_ingredient, name='update_ingredient'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
