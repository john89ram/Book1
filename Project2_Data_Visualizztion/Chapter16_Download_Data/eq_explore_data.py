import json

# Explore the structure of the data
filename = 'Chapter16_Download_Data/data/eq_data_1_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)

# Use this code to reformat the earthquake json files
#readable_file = 'Chapter16_Download_Data/data/readable_eq_data.json'
#with open(readable_file, 'w') as f:
#    json.dump(all_eq_data, f, indent=4)

# Finding all instances of earthquakes in the json file
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

# Extracting eq magnitudes
mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)

print(mags[:10])

# Extracting the locations of the eq

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])

