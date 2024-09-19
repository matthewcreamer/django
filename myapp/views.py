from rest_framework import generics
from django.http import HttpRequest
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, get_user_model
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.apps import apps
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from .utils import ExportCSV, ImportCSV
from .models import Owner, User, UserPermission, Exp, Merchant, MerchantArray, SlotMachine, SlotMachineItems, Mob, MobDrop, MobSkill
from .serializers import S_Owner, S_User, S_UserPermission, S_Exp, S_Merchant, S_MerchantArray, S_SlotMachine, S_SlotMachineItems, S_Mob, S_MobDrop, S_MobSkill
from .base import BasePermissionViewSet
from rest_framework import viewsets, status

class C_Exp(BasePermissionViewSet):
    queryset = Exp.objects.all()
    serializer_class = S_Exp

class C_Merchant(BasePermissionViewSet):
    queryset = Merchant.objects.all()
    serializer_class = S_Merchant

class C_MerchantArray(BasePermissionViewSet):
    queryset = MerchantArray.objects.all()
    serializer_class = S_MerchantArray

    def get_queryset(self):
        id_merchant = self.kwargs.get('id_merchant')
        if id_merchant is not None: return MerchantArray.objects.filter(id_merchant=id_merchant)
        return MerchantArray.objects.all()

class C_SlotMachine(BasePermissionViewSet):
    queryset = SlotMachine.objects.all()
    serializer_class = S_SlotMachine

    def get_queryset(self):
        tblidx = self.kwargs.get('tblidx')
        if tblidx is not None: return SlotMachine.objects.filter(tblidx=tblidx)
        return SlotMachine.objects.all()
    
class C_SlotMachineItems(BasePermissionViewSet):
    queryset = SlotMachineItems.objects.all()
    serializer_class = S_SlotMachineItems

    def get_queryset(self):
        id_slot_machine = self.kwargs.get('id_slot_machine')
        if id_slot_machine is not None: return SlotMachineItems.objects.filter(id_slot_machine=id_slot_machine)
        return SlotMachineItems.objects.all()

class C_Mob(BasePermissionViewSet):
    queryset = Mob.objects.all()
    serializer_class = S_Mob

    def get_queryset(self):
        tblidx = self.kwargs.get('tblidx')
        if tblidx is not None: return Mob.objects.filter(tblidx=tblidx)
        return Mob.objects.all()

class C_MobDrop(BasePermissionViewSet):
    queryset = MobDrop.objects.all()
    serializer_class = S_MobDrop

    def get_queryset(self):
        id_mob = self.kwargs.get('id_mob')
        if id_mob is not None: return MerchantArray.objects.filter(id_mob=id_mob)
        return MobDrop.objects.all()

class C_MobSkill(BasePermissionViewSet):
    queryset = MobSkill.objects.all()
    serializer_class = S_MobSkill

    def get_queryset(self):
        id_mob = self.kwargs.get('id_mob')
        if id_mob is not None: return MobSkill.objects.filter(id_mob=id_mob)
        return MobSkill.objects.all()

# class OwnerViewSet(viewsets.ModelViewSet):
#     queryset = Owner.objects.all()
#     serializer_class = S_Owner
#     permission_classes = [IsAuthenticated]

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = S_User
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user
#         if hasattr(user, 'owner'):
#             return User.objects.filter(owner=user)
#         return User.objects.none()

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

def C_ExportCSV(request: HttpRequest, model_name: str):
    return ExportCSV(request, model_name)

def C_ImportCSV(request: HttpRequest, model_name: str):
    return ImportCSV(request, model_name)

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def C_Login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return JsonResponse({'error': 'Username and password are required.'}, status=400)

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        request.session.save()

        if isinstance(user, User):
            excluded_tables = ['owner', 'user', 'userpermission', 'session', 'contenttype', 'group', 'permission', 'logentry']
            
            models = apps.get_models()
            
            for model in models:
                model_name = model._meta.model_name
                if model_name not in excluded_tables:
                    if not UserPermission.objects.filter(user=user, table=model_name).exists():
                        UserPermission.objects.create(user=user, table=model_name, get=False, put=False, post=False, delete=False)
        
        user_type = 'Owner' if isinstance(user, Owner) else 'User'
        return JsonResponse({'message': f'{user_type} {user.name} logged in successfully'})
    
    return JsonResponse({'error': 'Invalid credentials'}, status=400)

class C_UserPermission(BasePermissionViewSet):
    queryset = UserPermission.objects.all()
    serializer_class = S_UserPermission