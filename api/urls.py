from django.urls import path
from .views import obtener_agregar_items, editar_eliminar_item

urlpatterns = [
    path('items/', obtener_agregar_items, name='obtener_agregar_items'),
    path('items/<int:id>', editar_eliminar_item, name='editar_eliminar_item')
]