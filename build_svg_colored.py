import urllib.request
import json
import math

url = 'https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson'
print('Fetching GeoJSON...')
data = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))

INFO = {
    'Greenland': '0%',
    'Canada': '0.2%',
    'United States': '1%',
    'Mexico': '0%',
    'Venezuela': '0%',
    'Colombia': '0%',
    'Brazil': '30%',
    'Bolivia': '0%',
    'Paraguay': '0%',
    'Argentina': '0%',
    'Algeria': '0%',
    'Libya': '0%',
    'Mauritania': '0%',
    'Mali': '0%',
    'Niger': '0%',
    'Chad': '0%',
    'Nigeria': '0%',
    'Central African Republic': '0%',
    'Democratic Republic of the Congo': '0%',
    'Angola': '0%',
    'Namibia': '0%',
    'Egypt': '0%',
    'Sudan': '0%',
    'Ethiopia': '0%',
    'Kenya': '0%',
    'Tanzania': '0%',
    'Zambia': '0%',
    'Zimbabwe': '0%',
    'Mozambique': '0%',
    'Madagascar': '0%',
    'Turkey': '100%',
    'Syria': '0%',
    'Iraq': '0%',
    'Saudi Arabia': '0%',
    'Yemen': '0%',
    'Iran': '0%',
    'Afghanistan': '0%',
    'Pakistan': '0%',
    'India': '99%',
    'Kazakhstan': '0%',
    'Mongolia': '0%',
    'China': '75%',
    'Russia': '51%',
    'Myanmar': '0%',
    'Thailand': '0%',
    'Cambodia': '0%',
    'Australia': '33%',
    'United Kingdom': '38%',
    'France': '58%',
    'Spain': '68%',
    'Germany': '62%',
    'Poland': '64%',
    'Sweden': '75%'
}

def get_color(pct_str):
    if pct_str is None:
        return '#CBD5E1' # Gray default
    pct = float(pct_str.replace('%', ''))
    if pct == 100 or pct >= 95:
        return '#16A34A' # Green for ~100%
    elif pct == 0:
        return '#DC2626' # Red for 0%
    else:
        # Interpolate or light blue gradient for 1-90%
        # 1% -> light blue (#93C5FD), 75% -> deep sky blue (#0284C7)
        ratio = pct / 90.0
        r = int(147 + (2 - 147) * ratio)
        g = int(197 + (132 - 197) * ratio)
        b = int(253 + (199 - 253) * ratio)
        return f'#{r:02X}{g:02X}{b:02X}'

def project_equi(lon, lat):
    x = (lon + 180.0) * (1000.0 / 360.0)
    y = (90.0 - lat) * (500.0 / 180.0)
    return round(x, 1), round(y, 1)

paths = []
text_labels = []

# Specific label override positions for major countries so text is placed perfectly
LABEL_POSITIONS = {
    'United States': (210, 210),
    'Canada': (200, 140),
    'Brazil': (340, 340),
    'Russia': (680, 120),
    'China': (790, 220),
    'India': (715, 270),
    'Australia': (860, 390),
    'Greenland': (350, 60),
    'Argentina': (315, 420),
    'Algeria': (490, 230),
    'Kazakhstan': (680, 175),
    'Mongolia': (770, 160),
    'Saudi Arabia': (600, 250),
    'Egypt': (550, 220),
    'Turkey': (585, 195),
    'United Kingdom': (465, 145),
    'France': (485, 175),
    'Spain': (450, 205),
    'Germany': (525, 160),
    'Poland': (555, 155),
    'Sweden': (525, 110),
    'Indonesia': (820, 305),
    'Mexico': (180, 245),
    'South Africa': (545, 410)
}

for f in data['features']:
    name = f['properties']['name']
    if name == 'United States of America': name = 'United States'
    if name == 'Republic of Korea': name = 'South Korea'
    if name == 'United Republic of Tanzania': name = 'Tanzania'

    pct = INFO.get(name, None)
    color = get_color(pct)

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
        path_str = f'<path class="country-path" data-c="{name}" fill="{color}" d="' + ' '.join(d_parts) + f'"><title>{name} ({pct if pct else "N/A"})</title></path>'
        paths.append(path_str)
        
        # Determine center for label
        if name in LABEL_POSITIONS:
            cx, cy = LABEL_POSITIONS[name]
        elif pts_all:
            cx = round(sum(p[0] for p in pts_all) / len(pts_all), 1)
            cy = round(sum(p[1] for p in pts_all) / len(pts_all), 1)
        else:
            continue

        label_text = f'{name}'
        if pct:
            label_text += f' ({pct})'
            
        # Add text element for countries with electrification info or major countries
        if pct or name in LABEL_POSITIONS:
            text_labels.append(f'<text x="{cx}" y="{cy}" class="country-label">{label_text}</text>')

svg_content = '\n'.join(paths) + '\n<g class="labels-group">\n' + '\n'.join(text_labels) + '\n</g>'
with open('svg_paths.html', 'w', encoding='utf-8') as out:
    out.write(svg_content)

print(f'Successfully generated {len(paths)} country paths & {len(text_labels)} text labels in svg_paths.html')
