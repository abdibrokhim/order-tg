from django.contrib import admin

from .models import TGClient, Product, Tariff, Order


class TGClientAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'username', 'phone_number', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('tg_id', 'username', 'phone_number')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'username', 'phone_number', 'category', 'title',
                    'description', 'price', 'photo', 'ship', 'payment', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('tg_id', 'username', 'phone_number', 'category', 'title', 'description', 'price')


class TariffAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'duration', 'price', 'link')
    search_fields = ('name', 'quantity', 'duration', 'price')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'tariff', 'left_qty', 'created_at', 'left_days')
    search_fields = ('tg_id', 'tariff', 'left_qty', 'created_at', 'left_days')


admin.site.register(TGClient, TGClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tariff, TariffAdmin)
admin.site.register(Order, OrderAdmin)
