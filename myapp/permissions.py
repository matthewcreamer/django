from rest_framework.exceptions import PermissionDenied
from .models import UserPermission

def check_custom_permission(user, table, action):
    try:
        permission = user.permissions.get(table=table)
        if getattr(permission, action):
            return True
        else:
            raise PermissionDenied(f"You do not have {action} permission for {table}")
    except UserPermission.DoesNotExist:
        raise PermissionDenied("No permissions set for this table.")