from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
import json

# Base de datos en memoria (simulación)
items = [{"id": 1, "nombre": "Laptop"}, {"id": 2, "nombre": "Telefono"}]

@csrf_exempt # Desactiva la verificación CSRF para pruebas

def obtener_agregar_items(request):
    if request.method == 'GET': # Devolver la lista de ítems en formato JSON
        return JsonResponse(items, safe=False)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body) # Convertir JSON en diccionario
            nuevo_item = {
                "id": len(items) + 1,
                "nombre": data.get("nombre", "Sin nombre")
            }
            items.append(nuevo_item) # Agregar el nuevo ítem a la lista
            return JsonResponse(nuevo_item, status=201) # Respuesta
        except json.JSONDecodeError:
            return JsonResponse({"error": "Formato JSON inválido"}, status=400) 
         
        
@csrf_exempt
def get_editar_eliminar_item(request,id):
    if request.method == 'GET':
        elemento = next((item for item in items if item["id"] == id), None)
        if elemento:
            return JsonResponse(elemento, safe=False, status=201)   
        return JsonResponse({
            "info": "producto no encontrado",
        }, status=201)                     
    if request.method == 'PATCH':
        nombreViejo = ""
        try:
            data = json.loads(request.body)
            elemento = next((item for item in items if item["id"] == id), None)
            if elemento:
                nombreViejo = elemento["nombre"] 
                elemento["nombre"] = data["nombre"]
                return JsonResponse({
                    "id": id,
                    "nombre viejo": nombreViejo,
                    "nombre nuevo": elemento["nombre"]
                }, status=201)
            return JsonResponse({
                "info": "producto no encontrado",
            }, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Formato JSON inválido"}, status=400) 
    if request.method == 'DELETE':
        try:
            elemento = next((item for item in items if item["id"] == id), None)
            if elemento: 
                items.remove(elemento)
                return JsonResponse({
                    "ELIMINADO": elemento
                }, status=201)
            return JsonResponse({
                "info": "producto no encontrado",
            }, status=201)                
        except json.JSONDecodeError:
            return JsonResponse({"error": "Formato JSON inválido"}, status=400) 