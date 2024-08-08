from django.urls import path
from .views import download_csv, C_Exp, C_Merchant, C_MerchantArray, C_SlotMachine, C_SlotMachineArray, C_Mob

urlpatterns = [
    # EXP
    path('exp/', C_Exp.as_view(), name='exp'),
    path('exp/tblidx/<int:tblidx>/', C_Exp.as_view(), name='exp-tblidx'),

    # MERCHANT
    path('merchant/', C_Merchant.as_view(), name='merchant'),
    path('merchant/tblidx/<int:tblidx>/', C_Merchant.as_view(), name='merchant-tblidx'),

    path('merchant-array/', C_MerchantArray.as_view(), name='merchant-array'),

    # SLOT MACHINE
    path('slot-machine/', C_SlotMachine.as_view(), name='slot-machine'),
    path('slot-machine/tblidx/<int:tblidx>/', C_SlotMachine.as_view(), name='slot-machine-tblidx'),

    path('slot-machine-array/', C_SlotMachineArray.as_view(), name='slot-machine-array'),

    # MOB
    path('mob/', C_Mob.as_view(), name='mob'),
    path('mob/tblidx/<int:tblidx>/', C_Mob.as_view(), name='mob-tblidx'),

    # GENERATE CSV
    path('generate-csv/<str:model_name>/', download_csv, name='generate-csv'),
]