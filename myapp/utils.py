import csv
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.apps import apps
from django.db import models
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt

def ExportCSV(request, model_name):
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

def validate_csv_file(file):
    if not file.name.endswith('.csv'):
        raise ValidationError("File is not a CSV")

@csrf_exempt
def ImportCSV(request, model_name):
    if request.method == 'POST':
        model = apps.get_model('myapp', model_name) 
        csv_file = request.FILES['demo[]']
        validate_csv_file(csv_file)

        file_path = default_storage.save(csv_file.name, csv_file)

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                obj_data = {}
                for field in model._meta.get_fields():
                    field_name = field.name
                    value = row.get(field_name)
                    
                    if value is None:
                        continue

                    if isinstance(field, models.IntegerField) or isinstance(field, models.BigIntegerField):
                        try:
                            obj_data[field_name] = int(value)
                        except ValueError:
                            obj_data[field_name] = None
                    elif isinstance(field, models.FloatField) or isinstance(field, models.DecimalField):
                        try:
                            obj_data[field_name] = float(value)
                        except ValueError:
                            obj_data[field_name] = None
                    elif isinstance(field, models.DateField) or isinstance(field, models.DateTimeField):
                        try:
                            obj_data[field_name] = parse_date(value) 
                        except ValueError:
                            obj_data[field_name] = None
                    elif isinstance(field, models.BooleanField):
                        obj_data[field_name] = value.lower() in ['true', '1']
                    else:
                        obj_data[field_name] = value

                unique_fields = [field.name for field in model._meta.get_fields() if field.unique]
                filters = {field: obj_data[field] for field in unique_fields if field in obj_data}
                if not filters:
                    return JsonResponse({'error': 'No unique fields provided'}, status=400)

                model.objects.update_or_create(defaults=obj_data, **filters)

        return JsonResponse({'status': 'success'})

    return JsonResponse({'error': 'Invalid request'}, status=400)