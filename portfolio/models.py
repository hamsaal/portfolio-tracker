from django.db import models

# Create your models here.
class Asset(models.Model):
    ASSET_TYPE = [
        ('stock','Stock'),
        ('crypto', 'Crypto')
    ]

    ticker = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=100)
    asset_type=models.CharField(max_length = 10 , choices = ASSET_TYPE);
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticker} = {self.name}"

class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('buy', 'Buy'),
        ('sell','Sell')
    ]

    asset = models.ForeignKey(Asset,on_delete=models.CASCADE,related_name='transations')
    tx_type = models.CharField(max_length= 4 , choices=TRANSACTION_TYPE);
    quantity = models.DecimalField(max_digits=15,decimal_places=6);
    price_per_unit = models.DecimalField(max_digits=15, decimal_places=6);
    date = models.DateField()


    def __str__(self):
        return f"{self.tx_type} {self.quantity} {self.asset} @ {self.price_per_unit}"
