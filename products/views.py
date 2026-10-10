import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Products


@csrf_exempt
def get_products(request):
    products = Products.objects.all().order_by('-created_at')
    data = [
        {
            "id": product.id,
            "name": product.name,
            "price": str(product.price),
            "created_at": product.created_at.isoformat() if product.created_at else None,
        }
        for product in products
    ]
    return JsonResponse(data, safe=False)


@csrf_exempt
def create_product(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)

    name = data.get("name")
    price = data.get("price")

    if not name or price is None:
        return JsonResponse({"error": "name and price are required"}, status=400)

    product = Products.objects.create(name=name, price=price)
    return JsonResponse(
        {
            "id": product.id,
            "name": product.name,
            "price": str(product.price),
            "created_at": product.created_at.isoformat(),
        },
        status=201,
    )


@csrf_exempt
def get_product(request, id):
    product = get_object_or_404(Products, id=id)
    return JsonResponse(
        {
            "id": product.id,
            "name": product.name,
            "price": str(product.price),
            "created_at": product.created_at.isoformat(),
        }
    )


@csrf_exempt
def update_product(request, id):
    product = get_object_or_404(Products, id=id)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)

    if "name" in data:
        product.name = data["name"]
    if "price" in data:
        product.price = data["price"]

    product.save()
    return JsonResponse(
        {
            "id": product.id,
            "name": product.name,
            "price": str(product.price),
            "created_at": product.created_at.isoformat(),
        }
    )


@csrf_exempt
def patch_product(request, id):
    product = get_object_or_404(Products, id=id)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)

    for field, value in data.items():
        if field in ["name", "price"]:
            setattr(product, field, value)

    product.save()
    return JsonResponse(
        {
            "id": product.id,
            "name": product.name,
            "price": str(product.price),
            "created_at": product.created_at.isoformat(),
        }
    )


@csrf_exempt
def delete_product(request, id):
    product = get_object_or_404(Products, id=id)
    product.delete()
    return JsonResponse({"message": "Product deleted successfully"}, status=200)


@csrf_exempt
def products_api(request):
    if request.method == "GET":
        return get_products(request)
    if request.method == "POST":
        return create_product(request)
    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def product_detail_api(request, id):
    if request.method == "GET":
        return get_product(request, id)
    if request.method == "PUT":
        return update_product(request, id)
    if request.method == "PATCH":
        return patch_product(request, id)
    if request.method == "DELETE":
        return delete_product(request, id)
    return JsonResponse({"error": "Method not allowed"}, status=405)