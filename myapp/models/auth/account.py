from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group

class Owner(AbstractUser):
    name = models.CharField(max_length=16)

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='owner_permissions',  
        blank=True,
        help_text='Specific permissions for this owner.',
        related_query_name='owner'
    )
    groups = models.ManyToManyField(
        Group,
        related_name='owners',  
        blank=True,
        help_text='The groups this owner belongs to.',
        related_query_name='owner'
    )

    def __str__(self):
        return f"(Owner: {self.name})"

    class Meta:
        verbose_name = "Owner"
        verbose_name_plural = "Owners"

class User(AbstractUser):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='users')
    name = models.CharField(max_length=16)

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_permissions',  
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user'
    )
    groups = models.ManyToManyField(
        Group,
        related_name='users',  
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user'
    )

    def __str__(self):
        return f"(User: {self.name} under Owner: {self.owner.name})"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class UserPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='permissions')
    table = models.CharField(max_length=64)
    get = models.BooleanField(default=False)
    put = models.BooleanField(default=False)
    post = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)

    def __str__(self):
        return f"(User: {self.user.name}, Table: {self.table})"
