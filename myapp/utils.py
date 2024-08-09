import csv
from django.http import HttpResponse
from django.apps import apps
from django.db import models

def generate_csv(request, model_name):
    model = apps.get_model('myapp', model_name)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{model_name}.csv"'
    writer = csv.writer(response)
    excluded_fields = ['id']

    fields = [field.name for field in model._meta.fields if field.name not in excluded_fields]
    writer.writerow(fields)

    for obj in model.objects.all():
        row = []
        for field in fields:
            value = getattr(obj, field)
            field_instance = model._meta.get_field(field)

            if isinstance(field_instance, models.ForeignKey):
                related_field = field_instance.related_model._meta.pk.name
                value = getattr(value, related_field)
            else:
                value = str(value)

            row.append(value)
        writer.writerow(row)

    return response