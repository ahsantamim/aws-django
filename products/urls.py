from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.products_api, name="products_api"),
    path("products/<int:id>/", views.product_detail_api, name="product_detail_api"),
]