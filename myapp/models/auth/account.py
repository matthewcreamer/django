from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Owner(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=16)


    def __str__(self):
        return f"(Account: {self.name})"

class User(models.Model):
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='User')
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=16)
    

    def __str__(self):
        return f"(Account: {self.name})"
    
class UserPermission(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UserPermission')
    table = models.CharField(max_length=64)
    permission = models.CharField(max_length=16)
    

    def __str__(self):
        return f"(Account: {self.name})"

class Server(models.Model):
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='Server')
    name = models.CharField(max_length=16)
    

    def __str__(self):
        return f"(Account: {self.name})"