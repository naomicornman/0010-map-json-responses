import os
import json
fname = os.path.join('tempdata', 'googlemaps', 'stanford.json')

ffile = open(fname, 'r')
txt = ffile.read()
ffile.close()

address = json.loads(txt)

for x in address['results'][3]:
	print(x['formatted_address'])

for x in address['results']:
	print(x['geometry'])

ffile.close()
