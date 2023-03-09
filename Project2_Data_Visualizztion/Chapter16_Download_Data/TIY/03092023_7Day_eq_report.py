import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

dataset = 'Chapter16_Download_Data/TIY/tiy_data/03092023_7Day_eq_report.json'

with open(dataset, 'r', encoding='utf-8') as f:
    all_eq_data = json.load(f)

title = all_eq_data['metadata']['title']

eq_dictionaries = all_eq_data['features']

mags, lons, lats, info = [], [], [], []

for i in eq_dictionaries:
    mags.append(i['properties']['mag'])
    lons.append(i['geometry']['coordinates'][0])
    lats.append(i['geometry']['coordinates'][1])
    info.append(i['properties']['title'])

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': info,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Cividis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    }
}]

my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='Chapter16_Download_Data/TIY/tiy_data/03092023_7Day_eq_report.html')