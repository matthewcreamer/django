from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ..dbo_fields import UnsignedByteField, UnsignedWordField, UnsignedDwordField

class Mob(models.Model):
    tblidx = UnsignedDwordField(unique=True)
    

    def __str__(self):
        return f"(TBLIDX: {self.tblidx})"
        