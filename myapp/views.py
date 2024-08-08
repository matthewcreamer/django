from rest_framework import generics
from .models import ExpTable
from .serializers import S_ExpTable

# class C_ItemTable(generics.ListCreateAPIView):
#     queryset = ItemTable.objects.all()
#     serializer_class = S_ItemTable

#     def get_queryset(self):
#         tblidx = self.kwargs.get('tblidx')
#         if tblidx is not None: return ItemTable.objects.filter(tblidx=tblidx)
#         return ItemTable.objects.all()

class C_ExpTable(generics.ListCreateAPIView):
    queryset = ExpTable.objects.all()
    serializer_class = S_ExpTable

    def get_queryset(self):
        tblidx = self.kwargs.get('tblidx')
        if tblidx is not None: return ExpTable.objects.filter(tblidx=tblidx)
        return ExpTable.objects.all()
