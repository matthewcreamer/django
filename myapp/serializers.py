from .base import BaseSerializer
from rest_framework import serializers
from .models import Owner, User, UserPermission, Exp, Merchant, MerchantArray, SlotMachine, SlotMachineItems, Mob, MobDrop, MobSkill

class S_Exp(BaseSerializer):
    class Meta:
        model = Exp
        fields = '__all__'
        read_only_fields = ('owner',)  

class S_Merchant(BaseSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'

class S_MerchantArray(BaseSerializer):
    class Meta:
        model = MerchantArray
        fields = '__all__'

class S_SlotMachine(BaseSerializer):
    class Meta:
        model = SlotMachine
        fields = '__all__'

class S_SlotMachineItems(BaseSerializer):
    class Meta:
        model = SlotMachineItems
        fields = '__all__'

class S_Mob(BaseSerializer):
    class Meta:
        model = Mob
        fields = '__all__'

class S_MobDrop(BaseSerializer):
    class Meta:
        model = MobDrop
        fields = '__all__'

class S_MobSkill(BaseSerializer):
    class Meta:
        model = MobSkill
        fields = '__all__'

class S_Owner(BaseSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class S_User(BaseSerializer):
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
    
class S_UserPermission(BaseSerializer):
    class Meta:
        model = UserPermission
        fields = '__all__'