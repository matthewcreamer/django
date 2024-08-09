from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ..dbo_fields import UnsignedByteField, UnsignedWordField, UnsignedDwordField

class Mob(models.Model):
    tblidx = UnsignedDwordField(unique=True)
    dwMobGroup = UnsignedDwordField(default=0)
    wMob_Kind = UnsignedWordField(default=0)
    dwDrop_Zenny = UnsignedDwordField(default=0)
    fDrop_Zenny_Rate = models.FloatField(default=0)
    dwExp = UnsignedDwordField(default=0)
    byMob_Type = UnsignedByteField(default=0)
    drop_Item_Tblidx = UnsignedDwordField(default=0)
    bSize = UnsignedByteField(default=0)
    wTMQPoint = UnsignedWordField(default=0)
    dropQuestTblidx = UnsignedDwordField(default=0)
    dwUnknown = UnsignedDwordField(default=0)
    byUnknown = UnsignedByteField(default=0)
    byUnknown2 = UnsignedByteField(default=0)
    bShow_Name = UnsignedByteField(default=0)
    wSightAngle = UnsignedWordField(default=0)
    dwImmunity_Bit_Flag = UnsignedDwordField(default=0)
    bIsDragonBallDrop = UnsignedByteField(default=0)
    wMonsterClass = UnsignedWordField(default=0)
    wUseRace = UnsignedWordField(default=0)
    fRewardExpRate = models.FloatField(default=0)
    fRewardZennyRate = models.FloatField(default=0)
    dwFormulaOffset = UnsignedDwordField(default=0)
    fSettingRate_LP = models.FloatField(default=0)
    fSettingRate_LPRegen = models.FloatField(default=0)
    fSettingRate_PhyOffence = models.FloatField(default=0)
    fSettingRate_EngOffence = models.FloatField(default=0)
    fSettingRate_PhyDefence = models.FloatField(default=0)
    fSettingRate_EngDefence = models.FloatField(default=0)
    fSettingRate_AttackRate = models.FloatField(default=0)
    fSettingRate_DodgeRate = models.FloatField(default=0)
    fSettingPhyOffenceRate = models.FloatField(default=0)
    fSettingEngOffenceRate = models.FloatField(default=0)
    fSettingRate_Defence_Role = models.FloatField(default=0)
    bValidity_Able = UnsignedByteField(default=0)
    Name = UnsignedDwordField(default=0)
    wszNameText = models.CharField(max_length=255, blank=True, null=True)
    szModel = models.CharField(max_length=255, blank=True, null=True)
    byLevel = UnsignedByteField(default=0)
    byGrade = UnsignedByteField(default=0)
    dwAi_Bit_Flag = UnsignedDwordField(default=0)
    wLP_Regeneration = UnsignedWordField(default=0)
    wEP_Regeneration = UnsignedWordField(default=0)
    byAttack_Animation_Quantity = UnsignedByteField(default=0)
    byBattle_Attribute = UnsignedByteField(default=0)
    wBasic_Physical_Offence = UnsignedWordField(default=0)
    wBasic_Energy_Offence = UnsignedWordField(default=0)
    fWalk_Speed_Origin = UnsignedWordField(default=0)
    fWalk_Speed = models.FloatField(default=0)
    fRun_Speed_Origin = models.FloatField(default=0)
    fRun_Speed = models.FloatField(default=0)
    fRadius_X = models.FloatField(default=0)
    fRadius_Z = models.FloatField(default=0)
    wSight_Range = UnsignedWordField(default=0)
    wScan_Range = UnsignedWordField(default=0)
    byVisible_Sight_Range = UnsignedByteField(default=0)
    szCamera_Bone_Name = models.CharField(max_length=255, blank=True, null=True)
    wAttackCoolTime = UnsignedWordField(default=0)
    fFly_Height = models.FloatField(default=0)
    szNameText = models.CharField(max_length=255, blank=True, null=True)
    bSpawn_Animation = UnsignedByteField(default=0)
    dwDialogGroup = UnsignedDwordField(default=0)
    szILLust = models.CharField(max_length=255, blank=True, null=True)
    dwAllianceIdx = UnsignedDwordField(default=0)
    wAggroMaxCount = UnsignedWordField(default=0)
    dwNpcAttributeFlag = UnsignedDwordField(default=0)
    wStomachacheDefence = UnsignedWordField(default=0)
    wPoisonDefence = UnsignedWordField(default=0)
    wBleedDefence = UnsignedWordField(default=0)
    wBurnDefence = UnsignedWordField(default=0)

    
    def __str__(self):
        return f"(TBLIDX: {self.tblidx})"
    
class MobDrop(models.Model):
    id_mob = models.ForeignKey(Mob, on_delete=models.CASCADE, related_name='MobDrop')
    idxBigBag = UnsignedDwordField(default=0)
    byDropRate = UnsignedByteField(default=0)
    byTryCount = UnsignedByteField(default=0)


    def __str__(self):
        return f"(Mob ID: {self.id_mob})"
    
class MobSkill(models.Model):
    id_mob = models.ForeignKey(Mob, on_delete=models.CASCADE, related_name='MobSkill')
    wUse_Skill_Time = UnsignedWordField(default=0)
    use_Skill_Tblidx = UnsignedDwordField(default=0)
    byUse_Skill_Basis = UnsignedWordField(default=0)
    wUse_Skill_LP = UnsignedByteField(default=0)


    def __str__(self):
        return f"(Mob ID: {self.id_mob})"