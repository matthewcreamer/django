from rest_framework import generics, mixins, viewsets, status
from rest_framework.exceptions import NotFound
from django.http import HttpRequest
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from .utils import ExportCSV, ImportCSV
from .models import Owner, User, UserPermission, Exp, Merchant, MerchantArray, SlotMachine, SlotMachineArray, Mob, MobDrop, MobSkill
from .serializers import S_Owner, S_User, S_Exp, S_Merchant, S_MerchantArray, S_SlotMachine, S_SlotMachineArray, S_Mob, S_MobDrop, S_MobSkill

class C_Exp(viewsets.ModelViewSet):
    queryset = Exp.objects.all()
    serializer_class = S_Exp

    @action(detail=False, methods=['get'], url_path='tblidx/(?P<tblidx>\d+)')
    def filter_by_tblidx(self, request, tblidx=None):
        queryset = self.queryset.filter(tblidx=tblidx)
        if not queryset.exists():
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class C_Merchant(generics.ListCreateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = S_Merchant

    def get_queryset(self):
        tblidx = self.kwargs.get('tblidx')
        if tblidx is not None: return Merchant.objects.filter(tblidx=tblidx)
        return Merchant.objects.all()
    
class C_MerchantArray(generics.ListCreateAPIView):
    queryset = MerchantArray.objects.all()
    serializer_class = S_MerchantArray

    def get_queryset(self):
        id_merchant = self.kwargs.get('id_merchant')
        if id_merchant is not None: return MerchantArray.objects.filter(id_merchant=id_merchant)
        return MerchantArray.objects.all()

class C_SlotMachine(generics.ListCreateAPIView):
    queryset = SlotMachine.objects.all()
    serializer_class = S_SlotMachine

    def get_queryset(self):
        tblidx = self.kwargs.get('tblidx')
        if tblidx is not None: return SlotMachine.objects.filter(tblidx=tblidx)
        return SlotMachine.objects.all()
    
class C_SlotMachineArray(generics.ListCreateAPIView):
    queryset = SlotMachineArray.objects.all()
    serializer_class = S_SlotMachineArray

    def get_queryset(self):
        id_slot_machine = self.kwargs.get('id_slot_machine')
        if id_slot_machine is not None: return SlotMachineArray.objects.filter(id_slot_machine=id_slot_machine)
        return SlotMachineArray.objects.all()

class C_Mob(generics.ListCreateAPIView):
    queryset = Mob.objects.all()
    serializer_class = S_Mob

    def get_queryset(self):
        tblidx = self.kwargs.get('tblidx')
        if tblidx is not None: return Mob.objects.filter(tblidx=tblidx)
        return Mob.objects.all()

class C_MobDrop(generics.ListCreateAPIView):
    queryset = MobDrop.objects.all()
    serializer_class = S_MobDrop

    def get_queryset(self):
        id_mob = self.kwargs.get('id_mob')
        if id_mob is not None: return MerchantArray.objects.filter(id_mob=id_mob)
        return MobDrop.objects.all()

class C_MobSkill(generics.ListCreateAPIView):
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
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})