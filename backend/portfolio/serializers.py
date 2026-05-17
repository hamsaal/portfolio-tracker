from rest_framework import serializers
from .models import Asset, Transaction


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id', 'ticker', 'name', 'asset_type', 'created_at']


class TransactionSerializer(serializers.ModelSerializer):
    asset_ticker = serializers.CharField(source='asset.ticker', read_only=True)
    total_value = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = ['id', 'asset', 'asset_ticker', 'total_value','tx_type', 'quantity', 'price_per_unit', 'date']

    def get_total_value(self,obj):
        return obj.quantity * obj.price_per_unit