from django.http import JsonResponse
from django.views import View

from .models import Order


class OrderListView(View):
    def get(self, request):
        orders = Order.objects.select_related("product").all()
        data = [
            {
                "id": order.id,
                "product": {
                    "id": order.product.id,
                    "name": order.product.name,
                },
                "quantity": order.quantity,
                "status": order.status,
                "created_at": order.created_at.isoformat(),
            }
            for order in orders
        ]
        return JsonResponse(data, safe=False)
