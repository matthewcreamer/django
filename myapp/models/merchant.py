from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ..dbo_fields import UnsignedByteField, UnsignedWordField, UnsignedDwordField

class Merchant(models.Model):
    tblidx = UnsignedDwordField(unique=True)
    wszNameText = models.CharField(max_length=255, blank=True, null=True)
    bySell_Type = UnsignedByteField()
    Tab_Name = UnsignedDwordField()
    dwNeedMileage = UnsignedDwordField()
    

    def __str__(self):
        return f"(TBLIDX: {self.tblidx})"
        
class MerchantArray(models.Model):
    id_merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='MerchantArray')
    aItemTblidx = UnsignedDwordField()
    aNeedItemTblidx = UnsignedDwordField()
    abyNeedItemStack = UnsignedByteField()
    adwNeedZenny = UnsignedDwordField()
    

    def __str__(self):
        return f"(Merchant ID: {self.id_merchant})"