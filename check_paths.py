import re

f = open('svg_paths.html', 'r', encoding='utf-8').read()
print('Length of svg_paths.html:', len(f))
countries = ['India', 'China', 'United States', 'Canada', 'Brazil', 'Russia', 'France', 'Germany', 'Spain', 'Turkey', 'United Kingdom', 'Australia']
for c in countries:
    count = f.count(f'data-c="{c}"')
    print(f'{c}: {count}')
