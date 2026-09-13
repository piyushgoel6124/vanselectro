import re

with open('railway_map_clickable.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('id="prof0"')
end_idx = text.find('id="prof1"')
prof0_html = text[start_idx:end_idx]

print("=== PROF0 HTML ===")
print(prof0_html)
