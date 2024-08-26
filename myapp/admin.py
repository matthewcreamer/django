from django.contrib import admin
from .models import Owner, User, UserPermission

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'name', 'email')
    filter_horizontal = ('user_permissions', 'groups')  # Makes selection boxes for permissions/groups

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'owner', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'name', 'owner__name', 'email')
    filter_horizontal = ('user_permissions', 'groups')  # Makes selection boxes for permissions/groups

@admin.register(UserPermission)
class UserPermissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'get', 'put', 'post', 'delete')
    search_fields = ('user__name', 'table')
