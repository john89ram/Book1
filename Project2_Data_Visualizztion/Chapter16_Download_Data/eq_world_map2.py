import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data
filename = 'Chapter16_Download_Data/data/eq_data_30_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

#data = [Scattergeo(lon=lons, lat=lats)]

# This is a good wat to format when customization is important
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    # Adding more detail to show severity of the earthquake
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    }
}]
my_layout = Layout(title="Global Earthquakes")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='Chapter16_Download_Data/data/global_earthquakes2.html')
