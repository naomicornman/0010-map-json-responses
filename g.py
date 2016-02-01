import os
import json
fname = os.path.join('tempdata', 'mapzen', 'stanford.json')

ffile = open(fname, 'r')
txt = ffile.read()
ffile.close()

address = json.loads(txt)

for x in address['features']:
	print((x['properties']['label']),(';'),(x['properties']['confidence']),(';'),(x['geometry']['coordinates']))

ffile.close()
