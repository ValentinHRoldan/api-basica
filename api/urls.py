from django.urls import path
from .views import obtener_agregar_items, get_editar_eliminar_item

urlpatterns = [
    path('items/', obtener_agregar_items, name='obtener_agregar_items'),
    path('items/<int:id>', get_editar_eliminar_item, name='get_editar_eliminar_item')
]