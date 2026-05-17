from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Asset, Transaction


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['ticker', 'name', 'asset_type', 'created_at']
    search_fields = ['ticker', 'name']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['asset', 'tx_type', 'quantity', 'price_per_unit', 'date']
    list_filter = ['tx_type']