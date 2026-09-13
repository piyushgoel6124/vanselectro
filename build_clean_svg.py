import json

with open('countries.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Colors matching original reference map exactly:
# 100% / 99% -> Green (#16A34A)
# 0% -> Red (#DC2626)
# Mid values -> Light Blue (#3B82F6) / Sky Blue
# Unspecified -> Light Gray (#E2E8F0)

INFO = {
    'Greenland': '0%', 'Canada': '0.2%', 'United States': '1%', 'Mexico': '0%',
    'Venezuela': '0%', 'Colombia': '0%', 'Brazil': '30%', 'Bolivia': '0%',
    'Paraguay': '0%', 'Argentina': '0%', 'Algeria': '0%', 'Libya': '0%',
    'Mauritania': '0%', 'Mali': '0%', 'Niger': '0%', 'Chad': '0%',
    'Nigeria': '0%', 'Central African Republic': '0%', 'Democratic Republic of the Congo': '0%',
    'Angola': '0%', 'Namibia': '0%', 'Egypt': '0%', 'Sudan': '0%',
    'Ethiopia': '0%', 'Kenya': '0%', 'Tanzania': '0%', 'Zambia': '0%',
    'Zimbabwe': '0%', 'Mozambique': '0%', 'Madagascar': '0%', 'Turkey': '100%',
    'Syria': '0%', 'Iraq': '0%', 'Saudi Arabia': '0%', 'Yemen': '0%',
    'Iran': '0%', 'Afghanistan': '0%', 'Pakistan': '0%', 'India': '99%',
    'Kazakhstan': '0%', 'Mongolia': '0%', 'China': '75%', 'Russia': '51%',
    'Myanmar': '0%', 'Thailand': '0%', 'Cambodia': '0%', 'Australia': '33%',
    'United Kingdom': '38%', 'France': '58%', 'Spain': '68%', 'Germany': '62%',
    'Poland': '64%', 'Sweden': '75%'
}

# Accurate coordinate centroids for key countries to keep text strictly inside country borders
LABEL_POSITIONS = {
    'United States': (240, 150),
    'Canada': (220, 90),
    'Brazil': (340, 310),
    'Russia': (700, 75),
    'China': (780, 150),
    'India': (720, 195),
    'Australia': (850, 360),
    'Greenland': (350, 45),
    'Argentina': (305, 390),
    'Algeria': (490, 175),
    'Kazakhstan': (660, 120),
    'Mongolia': (760, 115),
    'Saudi Arabia': (590, 185),
    'Egypt': (545, 160),
    'Turkey': (575, 140),
    'Sweden': (525, 65),
    'Poland': (545, 115),
    'Germany': (515, 120),
    'France': (485, 135),
    'Spain': (455, 155),
    'United Kingdom': (465, 105),
    'Indonesia': (820, 260),
    'Mexico': (180, 175),
    'Sudan': (555, 190),
    'Libya': (515, 165),
    'Iran': (625, 155)
}

def get_color(pct_str):
    if not pct_str:
        return '#E2E8F0' # Light gray default for unspecified
    pct = float(pct_str.replace('%', ''))
    
    # Smooth continuous 3-color RGB gradient:
    # 0%   -> Pure Red (#DC2626 -> R:220, G:38, B:38)
    # 50%  -> Bright Sky Blue (#0284C7 -> R:2, G:132, B:199)
    # 100% -> Vibrant Green (#16A34A -> R:22, G:163, B:74)
    
    if pct <= 50:
        ratio = pct / 50.0
        r = int(220 + (2 - 220) * ratio)
        g = int(38 + (132 - 38) * ratio)
        b = int(38 + (199 - 38) * ratio)
    else:
        ratio = (pct - 50.0) / 50.0
        r = int(2 + (22 - 2) * ratio)
        g = int(132 + (163 - 132) * ratio)
        b = int(199 + (74 - 199) * ratio)
        
    return f'#{max(0, min(255, r)):02X}{max(0, min(255, g)):02X}{max(0, min(255, b)):02X}'

def project_equi(lon, lat):
    x = (lon + 180.0) * (1000.0 / 360.0)
    y = (90.0 - lat) * (500.0 / 180.0)
    return round(x, 1), round(y, 1)

paths = []
text_labels = []

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
    if gtype == 'Polygon': polys = [coords]
    elif gtype == 'MultiPolygon': polys = coords
    else: continue
        
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
        
        # Only add labels for major countries that fit inside borders
        if name in LABEL_POSITIONS:
            cx, cy = LABEL_POSITIONS[name]
            label_text = f'{name}'
            if pct: label_text += f' ({pct})'
            text_labels.append(f'<text x="{cx}" y="{cy}" class="country-label">{label_text}</text>')

svg_content = '\n'.join(paths) + '\n<g class="labels-group">\n' + '\n'.join(text_labels) + '\n</g>'
with open('svg_paths.html', 'w', encoding='utf-8') as out:
    out.write(svg_content)

print(f'Generated {len(paths)} paths and {len(text_labels)} centered labels in svg_paths.html')
