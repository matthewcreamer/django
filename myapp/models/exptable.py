from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ..dbo_fields import UnsignedByteField, UnsignedWordField, UnsignedDwordField

class ExpTable(models.Model):
    tblidx = UnsignedDwordField(unique=True)
    dwExp = UnsignedDwordField()
    dwNeed_Exp = UnsignedDwordField()
    wStageWinSolo = UnsignedWordField()
    wStageDrawSolo = UnsignedWordField()
    wStageLoseSolo = UnsignedWordField()
    wWinSolo = UnsignedWordField()
    wPerfectWinSolo = UnsignedWordField()
    wStageWinTeam = UnsignedWordField()
    wStageDrawTeam = UnsignedWordField()
    wStageLoseTeam = UnsignedWordField()
    wWinTeam = UnsignedWordField()
    wPerfectWinTeam = UnsignedWordField()
    wNormal_Race = UnsignedWordField()
    wSuperRace = UnsignedWordField()
    dwMobExp = UnsignedWordField()
    dwPhyDefenceRef = UnsignedDwordField()
    dwEngDefenceRef = UnsignedDwordField()
    dwMobZenny = UnsignedDwordField()

    def __str__(self):
        return f"(TBLIDX: {self.tblidx})"
        