import json

filename = 'data/all_month.geojson'
with open(filename, 'rb') as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

magm, mags, titles, lons, lats = [], [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    # magm = map(abs, mag)

    try:
        mags.append(abs(float(mag)))
    except:
        mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

# print(mags)
"""
print(mags[:10])
print(titles[:2])
print(lons[: 5])
print(lats[:5])
"""
