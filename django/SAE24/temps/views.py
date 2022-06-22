from django.shortcuts import render
from .models import Sensors, SensorsData
from .forms import SensorsForm
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.models import model_to_dict
import csv

def liste_sensors(request):
    sensors = Sensors.objects.all()
    return render(request, 'sensors/liste.html', {'sensors': sensors})

def liste_data(request):
    data = SensorsData.objects.all()
    return render(request, 'data/liste.html', {'data': data})

def modif_sensors(request, id):
    obj = Sensors.objects.get(id=id)
    objform = SensorsForm(model_to_dict(obj))
    if request.method == "POST":
        form = SensorsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/sensor/liste")
    else:
        return render(request, "sensors/modif.html", {"form": objform, "id": id})


def save_modif_sensors(request, id):
    objform = SensorsForm(request.POST)
    bak = Sensors.objects.get(id=id)
    if objform.is_valid():
        objform = objform.save(commit=False)
        objform.id = id
        objform.macaddr = bak.macaddr
        objform.piece = bak.piece
        objform.save()
        return HttpResponseRedirect("/sensors/liste")
    else:
        return render(request, "sensors/modif.html", {"form": objform, "id": id})


def filtre_par_sensor(request, id):
    data = SensorsData.objects.filter(sensor = id)
    return render(request, 'data/liste.html', {'data': data})


def export_csv(request, id):
    data = SensorsData.objects.filter(sensor = id)
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="export.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['timestamp', 'macaddr', 'piece', 'emplacement', 'nom', 'temp'])
    for i in data:
        writer.writerow(
            [i.datetime, 
            i.sensor.macaddr, 
            i.sensor.piece,
            i.sensor.emplacement,
            i.sensor.nom,
            i.temp])

    return response