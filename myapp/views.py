from rest_framework import generics
from django.http import HttpRequest
from .utils import generate_csv
from .models import Exp, Merchant, MerchantArray, SlotMachine, SlotMachineArray, Mob
from .serializers import S_Exp, S_Merchant, S_MerchantArray, S_SlotMachine, S_SlotMachineArray, S_Mob

class C_Exp(generics.ListCreateAPIView):
    queryset = Exp.objects.all()
    serializer_class = S_Exp

    def get_queryset(self):
        tblidx = self.kwargs.get('tblidx')
        if tblidx is not None: return Exp.objects.filter(tblidx=tblidx)
        return Exp.objects.all()

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

class C_Mob(generics.ListCreateAPIView):
    queryset = Mob.objects.all()
    serializer_class = S_Mob

    def get_queryset(self):
        tblidx = self.kwargs.get('tblidx')
        if tblidx is not None: return Mob.objects.filter(tblidx=tblidx)
        return Mob.objects.all()

def download_csv(request: HttpRequest, model_name: str):
    return generate_csv(request, model_name)
