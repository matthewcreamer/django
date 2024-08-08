from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ..dbo_fields import UnsignedByteField, UnsignedWordField, UnsignedDwordField

class ExpTable(models.Model):
    tblidx = models.IntegerField()
    name = models.CharField(max_length=255)
    exp = models.IntegerField()
    val = models.FloatField()
    val2 = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.IntegerField(
        validators = [MinValueValidator(0), MaxValueValidator(1)],
        default = 1
    )

    def __str__(self):
        return f"(TBLIDX: {self.tblidx})"
        