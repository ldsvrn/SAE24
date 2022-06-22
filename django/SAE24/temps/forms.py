from . import models
from django.forms import ModelForm

class SensorsForm(ModelForm):
    class Meta:
        model = models.Sensors
        fields = ('emplacement', 'nom')
        labels = {
            'nom': 'Nom',
            'emplacement': 'Emplacement'
        }