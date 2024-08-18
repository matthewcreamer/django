from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ..dbo_fields import UnsignedByteField, UnsignedWordField, UnsignedDwordField

class SlotMachine(models.Model):
    tblidx = UnsignedDwordField(unique=True)
    dwName = UnsignedDwordField()
    wszNameText = models.CharField(max_length=255, blank=True, null=True)
    szFile_Name = models.CharField(max_length=255, blank=True, null=True)
    byCoin = UnsignedByteField()
    bOnOff = UnsignedByteField()
    byType = UnsignedByteField()
    wfirstWinCoin = UnsignedWordField()


    def __str__(self):
        return f"(TBLIDX: {self.tblidx})"
    
class SlotMachineItems(models.Model):
    slot_machine = models.ForeignKey(SlotMachine, on_delete=models.CASCADE, related_name='slot_machine_items')
    aItemTblidx = UnsignedDwordField()
    byStack = UnsignedByteField()
    wQuantity = UnsignedWordField()


    def __str__(self):
        return f"(Slot Machine ID: {self.id_slot_machine})"
        