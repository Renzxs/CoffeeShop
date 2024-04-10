from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('stocks',views.view, name="view"),
     path('ingredients', views.show_ingredients, name="ingredients"),
    path('products',views.prod, name="prod"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
