import urllib.request
import json
import math

url = 'https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson'
print('Fetching GeoJSON...')
data = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))

def project(lon, lat):
    x = (lon + 180.0) * (1000.0 / 360.0)
    lat = max(-80.0, min(84.0, lat))
    phi = math.radians(lat)
    merchant_y = math.log(math.tan(math.pi / 4.0 + phi / 2.0))
    # Equirectangular or simple Mercator fit
    y = (1.0 - (lat + 90.0) / 180.0) * 500.0
    return round(x, 1), round(y, 1)

# Equirectangular projection is cleaner for standard world SVG maps: x = (lon + 180)/360 * 1000, y = (90 - lat)/180 * 500
def project_equi(lon, lat):
    x = (lon + 180.0) * (1000.0 / 360.0)
    y = (90.0 - lat) * (500.0 / 180.0)
    return round(x, 1), round(y, 1)

paths = []
country_centroids = {}

for f in data['features']:
    name = f['properties']['name']
    # Normalize name to match INFO dictionary if needed
    if name == 'United States of America': name = 'United States'
    if name == 'Republic of Korea': name = 'South Korea'
    if name == 'United Republic of Tanzania': name = 'Tanzania'

    geom = f['geometry']
    gtype = geom['type']
    coords = geom['coordinates']
    
    d_parts = []
    if gtype == 'Polygon':
        polys = [coords]
    elif gtype == 'MultiPolygon':
        polys = coords
    else:
        continue
        
    pts_all = []
    for poly in polys:
        for ring in poly:
            if not ring or len(ring) < 3: continue
            pt0 = project_equi(ring[0][0], ring[0][1])
            d_ring = [f'M{pt0[0]} {pt0[1]}']
            for pt in ring[1:]:
                pxy = project_equi(pt[0], pt[1])
                d_ring.append(f'L{pxy[0]} {pxy[1]}')
                pts_all.append(pxy)
            d_ring.append('Z')
            d_parts.append(' '.join(d_ring))
            
    if d_parts:
        path_str = f'<path class="country-path" data-c="{name}" d="' + ' '.join(d_parts) + f'"><title>{name}</title></path>'
        paths.append(path_str)
        if pts_all:
            avg_x = sum(p[0] for p in pts_all) / len(pts_all)
            avg_y = sum(p[1] for p in pts_all) / len(pts_all)
            country_centroids[name] = (round(avg_x, 1), round(avg_y, 1))

svg_content = '\n'.join(paths)
with open('svg_paths.html', 'w', encoding='utf-8') as out:
    out.write(svg_content)

print(f'Successfully wrote {len(paths)} SVG paths to svg_paths.html')
