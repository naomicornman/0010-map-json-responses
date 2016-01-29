import json
import os
fname = os.path.join('tempdata', 'googlemaps', 'stanford.json')

ffile = open(fname, 'r')
txt = ffile.read()


mydict = json.loads(txt)
# type(mydata)
print(dict['status'])
ffile.close()