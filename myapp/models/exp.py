from django.db import models
from django.contrib.auth.models import Group
from django.core.validators import MaxValueValidator, MinValueValidator
from ..dbo_fields import UnsignedByteField, UnsignedWordField, UnsignedDwordField
from .auth.account import Owner

class Exp(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='exp_owner')
    
    tblidx = UnsignedDwordField(unique=True)
    dwExp = UnsignedDwordField(default=0)
    dwNeed_Exp = UnsignedDwordField(default=0)
    wStageWinSolo = UnsignedWordField(default=0)
    wStageDrawSolo = UnsignedWordField(default=0)
    wStageLoseSolo = UnsignedWordField(default=0)
    wWinSolo = UnsignedWordField(default=0)
    wPerfectWinSolo = UnsignedWordField(default=0)
    wStageWinTeam = UnsignedWordField(default=0)
    wStageDrawTeam = UnsignedWordField(default=0)
    wStageLoseTeam = UnsignedWordField(default=0)
    wWinTeam = UnsignedWordField(default=0)
    wPerfectWinTeam = UnsignedWordField(default=0)
    wNormal_Race = UnsignedWordField(default=0)
    wSuperRace = UnsignedWordField(default=0)
    dwMobExp = UnsignedWordField(default=0)
    dwPhyDefenceRef = UnsignedDwordField(default=0)
    dwEngDefenceRef = UnsignedDwordField(default=0)
    dwMobZenny = UnsignedDwordField(default=0)
    

    def __str__(self):
        return f"(TBLIDX: {self.tblidx})"
        