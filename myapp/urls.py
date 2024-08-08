from django.urls import path
from .views import C_ExpTable

urlpatterns = [
    path('exptable/', C_ExpTable.as_view(), name='exp-table'),
    path('exptable/tblidx/<int:tblidx>/', C_ExpTable.as_view(), name='exp-table-tblidx'),
]