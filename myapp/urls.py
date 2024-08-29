from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import get_csrf_token, C_Login, C_UserPermission, C_ExportCSV, C_ImportCSV, C_Exp, C_Merchant, C_MerchantArray, C_SlotMachine, C_SlotMachineItems, C_Mob, C_MobDrop, C_MobSkill

router = DefaultRouter()
router.register(r'exp', C_Exp, basename='exp')
router.register(r'user-permission', C_UserPermission, basename='user-permission')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', C_Login, name='login'),
]

# urlpatterns = [
#     # EXP
#     path('exp/', C_Exp.as_view(), name='exp'),
#     path('exp/tblidx/<int:tblidx>/', C_Exp.as_view(), name='exp-tblidx'),

#     # MERCHANT
#     path('merchant/', C_Merchant.as_view(), name='merchant'),
#     path('merchant/tblidx/<int:tblidx>/', C_Merchant.as_view(), name='merchant-tblidx'),

#     path('merchant-array/', C_MerchantArray.as_view(), name='merchant-array'),
#     path('merchant-array/id_merchant/<int:id_merchant>/', C_MerchantArray.as_view(), name='merchant-array-parent'),

#     # SLOT MACHINE
#     path('slot-machine/', C_SlotMachine.as_view(), name='slot-machine'),
#     path('slot-machine/tblidx/<int:tblidx>/', C_SlotMachine.as_view(), name='slot-machine-tblidx'),

#     path('slot-machine-array/', C_SlotMachineItems.as_view(), name='slot-machine-array'),
#     path('slot-machine-array/id_slot_machine/<int:id_slot_machine>/', C_SlotMachineItems.as_view(), name='slot-machine-array-parent'),

#     # MOB
#     path('mob/', C_Mob.as_view(), name='mob'),
#     path('mob/tblidx/<int:tblidx>/', C_Mob.as_view(), name='mob-tblidx'),

#     path('mob-drop/', C_MobDrop.as_view(), name='mob-drop'),
#     path('mob-drop/id_mob/<int:id_mob>/', C_MobDrop.as_view(), name='mob-drop'),

#     path('mob-skill/', C_MobDrop.as_view(), name='mob-skill'),
#     path('mob-skill/id_mob/<int:id_mob>/', C_MobDrop.as_view(), name='mob-skill'),

#     # EXPORT CSV
#     path('export-csv/<str:model_name>/', C_ExportCSV, name='export-csv'),

#     # IMPORT CSV
#     path('import-csv/<str:model_name>/', C_ImportCSV, name='import-csv'),

#     # GENERATE CSRF TOKEN
#     path('csrf-token/', get_csrf_token, name='get_csrf_token'),
# ]