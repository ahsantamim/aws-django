from django.contrib import admin
from .models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_at')
    list_display_links = ('name',)
    ordering = ('created_at',)