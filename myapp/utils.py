import csv
from django.http import HttpResponse
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist

def generate_csv(request, model_name):
    try:
        if model_name == 'SlotMachine':
            slot_machine_model = apps.get_model('myapp', 'SlotMachine')
            slot_machine_array_model = apps.get_model('myapp', 'SlotMachineArray')

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="slot_machines.csv"'

            writer = csv.writer(response)

            slot_machine_fields = [field.name for field in slot_machine_model._meta.fields]
            slot_machine_array_fields = [field.name for field in slot_machine_array_model._meta.fields if field.name != 'slot_machine']

            writer.writerow(slot_machine_fields + slot_machine_array_fields)

            slot_machines = slot_machine_model.objects.all()
            for slot_machine in slot_machines:
                slot_machine_data = [getattr(slot_machine, field) for field in slot_machine_fields]
                writer.writerow(slot_machine_data)

                slot_machine_arrays = slot_machine.arrays.all()
                for array in slot_machine_arrays:
                    array_data = [getattr(array, field) for field in slot_machine_array_fields]
                    writer.writerow([''] * len(slot_machine_fields) + array_data)

            return response

        else:
            model = apps.get_model('myapp', model_name)

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{model_name}.csv"'

            writer = csv.writer(response)

            fields = [field.name for field in model._meta.fields]
            writer.writerow(fields)

            for obj in model.objects.all().values_list():
                writer.writerow(obj)

            return response

    except LookupError:
        return HttpResponse(f"Model '{model_name}' not found.", status=404)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)
