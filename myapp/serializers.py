from rest_framework import serializers
from .models import Exp, Merchant, MerchantArray, SlotMachine, SlotMachineArray, Mob, MobDrop, MobSkill

class S_Exp(serializers.ModelSerializer):
    class Meta:
        model = Exp
        fields = '__all__'

class S_Merchant(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'

class S_MerchantArray(serializers.ModelSerializer):
    class Meta:
        model = MerchantArray
        fields = '__all__'

class S_SlotMachine(serializers.ModelSerializer):
    class Meta:
        model = SlotMachine
        fields = '__all__'

class S_SlotMachineArray(serializers.ModelSerializer):
    class Meta:
        model = SlotMachineArray
        fields = '__all__'

class S_Mob(serializers.ModelSerializer):
    class Meta:
        model = Mob
        fields = '__all__'

class S_MobDrop(serializers.ModelSerializer):
    class Meta:
        model = MobDrop
        fields = '__all__'

class S_MobSkill(serializers.ModelSerializer):
    class Meta:
        model = MobSkill
        fields = '__all__'