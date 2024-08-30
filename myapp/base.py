from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import models
from .models import Owner, User, UserPermission

class BasePermissionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        model_name = self.queryset.model._meta.model_name

        if isinstance(user, Owner):
            if model_name == 'userpermission':
                return self.queryset.filter(user__in=user.users.all())  
            return self.queryset.filter(owner=user)

        elif isinstance(user, User):
            if model_name == 'userpermission':
                return self.queryset.filter(user=user)
            return self.queryset.filter(owner=user.owner)

        return self.queryset.none()

    def has_permission(self, user, action, table_name):
        if isinstance(user, Owner):
            return True
        elif isinstance(user, User):
            try:
                permission = UserPermission.objects.get(user=user, table=table_name)
                return getattr(permission, action, False)
            except UserPermission.DoesNotExist:
                return False
        return False

    def check_permissions(self, request):
        user = request.user
        action = self.determine_action(request)
        table_name = self.queryset.model._meta.model_name

        if table_name == 'userpermission' and isinstance(user, Owner):
            return
        
        if not self.has_permission(user, action, table_name):
            print(f"Permission denied for user: {user}, action: {action}, table: {table_name}")
            self.permission_denied(request)

    def determine_action(self, request):
        method = request.method.lower()
        if method == 'get':
            return 'get'
        elif method == 'post':
            return 'post'
        elif method == 'put':
            return 'put'
        elif method == 'delete':
            return 'delete'
        return 'unknown'

    def list(self, request, *args, **kwargs):
        self.check_permissions(request)
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.check_permissions(request)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.check_permissions(request)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.check_permissions(request)
        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=['get'], url_path=r'tblidx/(?P<tblidx>\d+)')
    def filter_by_tblidx(self, request, tblidx=None):
        queryset = self.get_queryset().filter(tblidx=tblidx)
        if not queryset.exists():
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class BaseSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        for field in self.Meta.model._meta.fields:
            if field.name not in data or data[field.name] is None:
                default = field.get_default()
                if default is not models.NOT_PROVIDED:
                    data[field.name] = default
        return super().to_internal_value(data)

    def create(self, validated_data):
        request = self.context.get('request')

        if request and request.user:
            if hasattr(request.user, 'owner'):
                validated_data['owner'] = request.user.owner
            else:
                validated_data['owner'] = request.user

        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request')

        if request and request.user:
            if hasattr(request.user, 'owner'):
                instance.owner = request.user.owner
            else:
                instance.owner = request.user

        return super().update(instance, validated_data)