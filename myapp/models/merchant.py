from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ..dbo_fields import UnsignedByteField, UnsignedWordField, UnsignedDwordField

class Merchant(models.Model):
    tblidx = UnsignedDwordField(unique=True)
    wszNameText = models.CharField(max_length=255, blank=True, null=True)
    bySell_Type = UnsignedByteField(default=0)
    Tab_Name = UnsignedDwordField(default=0)
    dwNeedMileage = UnsignedDwordField(default=0)
    

    def __str__(self):
        return f"(TBLIDX: {self.tblidx})"
        
class MerchantArray(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='merchant_array')
    aItemTblidx = UnsignedDwordField(default=0)
    aNeedItemTblidx = UnsignedDwordField(default=0)
    abyNeedItemStack = UnsignedByteField(default=0)
    adwNeedZenny = UnsignedDwordField(default=0)
    

    def __str__(self):
        return f"(Merchant ID: {self.id_merchant})"