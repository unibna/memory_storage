import folium
from folium.plugins import MousePosition

from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy

from django.contrib.gis.geos import Point
from django.views.generic import CreateView, DetailView

from .models import Memory
from .forms import MemoryCreateForm


base_map = {
    'Google Maps': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Maps',
        overlay = True,
        control = True
    )
}

class MemoryCreate(CreateView):
    model = Memory
    template_name = 'memory/create.html'
    form_class = MemoryCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = self.request.user
        if user.is_anonymous:
            raise PermissionDenied
        
        # auto add user'info to the memory
        form.instance.author = user
        return super().form_valid(form)


def get_geo_location(memory):
    # parse location fields to get location point
    points = list((memory.location.coords))
    # reverse the position of lat and lon
    return points[::-1]


class MemoryDetail(DetailView):
    model = Memory
    template_name = 'memory/detail.html'

    def get_context_data(self, *arg, **kwargs):
        context = super().get_context_data(*arg, **kwargs)
        points = get_geo_location(context['memory'])
        
        # create a map to display
        geo_map = folium.Map(location=points, zoom_start=8)
        # mark the location on the map
        folium.Marker(location=points).add_to(geo_map)
        # use google maps to display
        base_map['Google Maps'].add_to(geo_map)

        formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
        MousePosition(
            position="topright",
            separator=" | ",
            empty_string="NaN",
            lng_first=True,
            num_digits=20,
            prefix="Coordinates:",
            lat_formatter=formatter,
            lng_formatter=formatter,
        ).add_to(geo_map)

        geo_map = geo_map._repr_html_()
        context['map'] = geo_map

        return context
