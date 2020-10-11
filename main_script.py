# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:38:22 2020

@author: Fabian
"""
import uuid
import csv
from LatLon23 import LatLon, Longitude, Latitude, string2latlon
import pyproj


with open('file.xml', 'w') as f:
    print("<?xml version=\"1.0\"?>\n<FSData version=\"9.0\">", file=f)
f.close()
            
with open('Bergnamen.cup', newline='', encoding="ANSI") as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     for row in spamreader:
        if ("name" != row[0]) and ("-----Related Tasks-----" != row[0]):
            #print(', '.join(row))
            print(row[0]) #Name
            print(row[3]) #Lat DDMM.MMM
            print(row[4]) #Long DDDMM.MMM
            print(row[5]) #Height m
            print(str(uuid.uuid1()))
            latdeg = row[3][:2]
            print(latdeg)
            latmin = row[3][2:].replace('N', '')
            print(latmin)
            longdeg = row[4][:3]
            print(longdeg)
            longmin = row[4][3:].replace('E', '')
            print(longmin)
            
            latlonobj = LatLon(Latitude(degree = latdeg, minute =latmin),Longitude(degree = longdeg, minute = longmin))
            print(latlonobj.to_string('D')) # Print coordinates to degree minute second
            
            
            lat = str(latlonobj.lat)
            long = str(latlonobj.lon)
            alt = float(row[5].replace('m', ''))*0.1
            alt = str(alt)
            newline = "	<LandmarkLocation instanceId=\"{" + str(uuid.uuid1()) + "}\" type=\"POI\" name=\"" +  row[0] + "\" lat=\"" + lat + "\" lon=\"" + long + "\" alt=\"" + alt + "\"/>"
            with open('file.xml','a') as f:
                print(newline, file=f)
            f.close()  
with open('file.xml', 'a') as f:
    print("</FSData>", file=f)
f.close()
"""
<?xml version="1.0"?>
<FSData version="9.0">
	<LandmarkLocation instanceId="{CD544AFF-EF0D-4398-BA1F-5510298690E2}" type="POI" name="Zugspitzetest" lat="47.42111976520967" lon="10.98492037240454" alt="2913.99726566113532"/>
</FSData>
"""