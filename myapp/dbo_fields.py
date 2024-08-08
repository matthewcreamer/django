from django.db import models
from django.core.exceptions import ValidationError

class UnsignedByteField(models.IntegerField):
    description = "Unsigned Byte (0 to 255)"

    def db_type(self, connection):
        if connection.vendor == 'mysql':
            return 'tinyint UNSIGNED'
        else:
            return super().db_type(connection)

    def validate(self, value, model_instance):
        if not (0 <= value <= 255):
            raise ValidationError(f'Value for {self.description} must be between 0 and 255')
        super().validate(value, model_instance)

class UnsignedWordField(models.IntegerField):
    description = "Unsigned Word (0 to 65,535)"

    def db_type(self, connection):
        if connection.vendor == 'mysql':
            return 'smallint UNSIGNED'
        else:
            return super().db_type(connection)

    def validate(self, value, model_instance):
        if not (0 <= value <= 65535):
            raise ValidationError(f'Value for {self.description} must be between 0 and 65535')
        super().validate(value, model_instance)

class UnsignedDwordField(models.IntegerField):
    description = "Unsigned Dword (0 to 4,294,967,295)"

    def db_type(self, connection):
        if connection.vendor == 'mysql':
            return 'int UNSIGNED'
        else:
            return super().db_type(connection)

    def validate(self, value, model_instance):
        if not (0 <= value <= 4294967295):
            raise ValidationError(f'Value for {self.description} must be between 0 and 4294967295')
        super().validate(value, model_instance)
