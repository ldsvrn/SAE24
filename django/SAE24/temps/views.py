from django.shortcuts import render
from .models import Sensors, SensorsData
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict

def liste_sensors(request):
    sensors = Sensors.objects.all()
    return render(request, 'sensors/liste.html', {'sensors': sensors})

def liste_data(request):
    data = SensorsData.objects.all()
    return render(request, 'data/liste.html', {'data': data})

def modif_sensors(request, id):
    obj = models.Sensors.objects.get(id=id)
    objform = SensorsForm(model_to_dict(obj))
    if request.method == "POST":
        form = AvionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/sensor/liste")
    else:
        return render(request, "sensors/modif.html", {"form": objform, "id": id})


def save_modif_sensors(request, id):
    objform = SensorsForm(request.POST)
    if objform.is_valid():
        objform = objform.save(commit=False)
        objform.id = id
        objform.save()
        return HttpResponseRedirect("/sensors/liste")
    else:
        return render(request, "sensors/modif.html", {"form": objform, "id": id})