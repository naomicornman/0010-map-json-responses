import json
import os
fname = os.path.join('tempdata', 'googlemaps', 'stanford.json')

ffile = open(fname, 'r')
txt = ffile.read()
ffile.close()

mydict = json.loads(txt)

# type(mydict)

print(mydict['status'])
ffile.close()