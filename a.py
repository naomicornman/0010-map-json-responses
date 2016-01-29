import requests
import os
URL = 'http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'
resp = requests.get(URL)
fname = os.path.join('tempdata', 'googlemaps', 'stanford.json')
ffile = open(fname, 'wb')
ffile.write(resp.content)
ffile.close()

print (("Downloading from : ") + (resp.url))

ffile = open(fname, 'r')
line_num = 0
for x in ffile:
    line_num += 1
ffile.close()

print(fname, "has", line_num, "lines")
	
print(fname, "has", (len(resp.text)), "characters")

ffile.close()



URL2 = 'http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json'
resp = requests.get(URL2)
mapname = os.path.join('tempdata', 'mapzen', 'stanford.json')
mapfile = open(mapname, 'wb')
mapfile.write(resp.content)

print (("Downloading from : ") + (resp.url))

mapfile = open(mapname, 'r')
line_num = 0
for x in mapfile:
    line_num += 1
mapfile.close()

print("Writing to:" + mapname)

print ("Wrote " + str(line_num) + "lines and " + str((len(resp.text))) + " characters")

# print(mapname, "has", line_num, "lines")
	
# print(mapname, "has", (len(resp.text)), "characters")

# mapfile.close()