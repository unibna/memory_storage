from django.forms import widgets
import floppyforms.__future__ as forms
from .models import Memory


class PointWidget(forms.gis.PointWidget, forms.gis.BaseGMapWidget):
        google_maps_api_key = 'AIzaSyB_kh8AQ4HmU3N2Bco3stQESFx2C9l-uN4'


class MemoryCreateForm(forms.ModelForm):

    class Meta:
        model = Memory
        fields = ['name', 'comment', 'location']
        widgets = {
            'location': PointWidget(attrs={'map_width': 600,}),
        }