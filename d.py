import os
import json
fname = os.path.join('tempdata', 'googlemaps', 'stanford.json')

ffile = open(fname, 'r')
txt = ffile.read()
ffile.close()

address = json.loads(txt)

# for ffile, address in dict.items():

for x in (address['results']):
	print((x['address_components'][0]['long_name']) + ('; ') + (x['address_components'][1]['long_name'])+ ('; ') + (x['address_components'][2]['long_name']) + ('; ') + (x['address_components'][3]['long_name']))
	print("")
	ffile.close()
