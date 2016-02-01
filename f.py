import os
import json
fname = os.path.join('tempdata', 'mapzen', 'stanford.json')

ffile = open(fname, 'r')
txt = ffile.read()
ffile.close()

address = json.loads(txt)

print(("type:"),(address['type']))

print(("text:"),(address['geocoding']['query']['text']))

print(("size:"),(address['geocoding']['query']['size']))

print(("boundary.country:"),(address['geocoding']['query']['boundary.country']))

ffile.close()
