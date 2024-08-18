from rest_framework import serializers
from .models import Owner, User, UserPermission, Exp, Merchant, MerchantArray, SlotMachine, SlotMachineItems, Mob, MobDrop, MobSkill

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

class S_SlotMachineItems(serializers.ModelSerializer):
    class Meta:
        model = SlotMachineItems
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

class S_Owner(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class S_User(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        owner = self.context['request'].user
        if self.instance is None:  
            if User.objects.filter(owner=owner).count() >= 3:
                raise serializers.ValidationError("You can only create up to 3 users.")
        return data