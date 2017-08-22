#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# BytingTheBigApple.py
# This script will download LION and Amdin Shapefiles from DCP's Bytes of The
# Big Apple Page.
#
# C:\Python27\ArcGIS10.4\python.exe C:\GitHub\Python\byting_the_big_apple\BytingTheBigApple.py
#
# ---------------------------------------------------------------------------
import os, json, csv, datetime, timeit, urllib2, shutil, zipfile, arcpy, glob
from zipfile import *

title = """
        (
       (_)
       ###
       (#c     _\\|/_
        #\\     wWWWw
        \\ \\-. (/. .\\)
        /\\ /`\\/\\   /\\           Byting The Big Apple
        |\\/   \\_) (_|
        `\\.' ; ;    ;`\\
          `\\;  ;    .  ;/\\
            `\\;    ;  ;|  \\
             ;   .' '  ;  /
             |_.'   ;  | /)
             (     ''._;'`
             |    ' . ;
             |.-'   .:)
             |        |
             (  .'  : |
             |,-  .:: |
             | ,-'  .;|
            _/___,_.:_\\_
           [I_I_I_I_I_I_]
           | __________ |
           | || |  | || |
          _| ||_|__|_|| |_
         /=--------------=\\
        /                  \\
       |                    |
        """
root = os.path.abspath(os.path.curdir)
data = {
   "list":[
      {
         "file":"nyad_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyad_",
         "name":"State_Assembly_Districts"
      },
      {
         "file":"nybb_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nybb_",
         "name":"Borough_Boundary"
      },
      {
         "file":"nycc_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycc_",
         "name":"City_Council_Disrtricts"
      },
      {
         "file":"nycd_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycd_",
         "name":"Community_Districts"
      },
      {
         "file":"nycg_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycg_",
         "name":"US_Congressional_Districts"
      },
      {
         "file":"nyed_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyed_",
         "name":"Election_Districts"
      },
      {
         "file":"nyfb_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyfb_",
         "name":"Fire_Battalions"
      },
      {
         "file":"nyfc_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyfc_",
         "name":"Fire_Companies"
      },
      {
         "file":"nyfd_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyfd_",
         "name":"Fire_Divisions"
      },
      {
         "file":"nyha_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyha_",
         "name":"Health_Area"
      },
      {
         "file":"nymc_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nymc_",
         "name":"Municipal_Court_Districts"
      },
      {
         "file":"nypp_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nypp_",
         "name":"Police_Precincts"
      },
      {
         "file":"nysd_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nysd_",
         "name":"School_Districts"
      },
      {
         "file":"nyss_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyss_",
         "name":"State_Senate_Districts"
      },
      {
         "file":"nycb2000_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycb2000_",
         "name":"Census_Blocks_2000"
      },
      {
         "file":"nycb2010_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycb2010_",
         "name":"Census_Blocks_2010"
      },
      {
         "file":"nyct2000_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyct2000_",
         "name":"Census_Tracts_2000"
      },
      {
         "file":"nyct2010_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyct2010_",
         "name":"Census_Tracks_2010"
      },
      {
         "file":"nyclion_",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyclion_",
         "name":"LION"
      }
   ]
}
# Clears out old folder.
def manage_directories(d, l):
    #creates or replaces drectories
    for i in d['list']:
        if os.path.exists(i['file']+l):
            shutil.rmtree(root + '/' + i['file']+l)

    for i in glob.glob("*.gdb"):
        shutil.rmtree(i)

    for i in glob.glob("*.zip"):
        shutil.rmtree(i)
# Gathers data from Bytes of The Big Apple and Unzips it.
# Also makes the LION gdb
def byting(d, l):
    #used to over come proxy issue in the office
    proxy = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)

    #loop our list of gtfs we need to download
    for i in d['list']:
        try:
            f = urllib2.urlopen(i['url'] + l + '.zip')
            data = f.read()
            with open(i['file']+ l + ".zip", "wb") as code:
                code.write(data)
            #extracts zips to ALL-GTFS folders then removes the zip.
            with zipfile.ZipFile(root + '/' + i['file'] + l.upper() + '.zip', "r") as z:
                z.extractall(root)
            #removes zip
            print("    " + i['file'] + l+ " Downloaded and Unzipped")
            os.remove(i['file'] + l + ".zip")
        except urllib2.HTTPError:
            pass

    #rename files to include the version of lion
    folders = os.walk(root).next()[1]
    folders.remove('lion')
    for i in folders:
        files = os.listdir(i)
        for j in files:
            if ('nycb2000' in j) or ('nycb2010' in j) or ('nyct2000' in j) or ('nyct2010' in j):
                rj = j[:8] + '_' + l.upper() + j[-4:]
                origin = root + '/'+ i + '/' + j
                rename = root + '/'+ i + '/' + rj
                shutil.move(origin , rename)
            else:
                rj = j[:4] + '_' + l.upper() +  j[4:]
                origin = root + '/'+ i + '/' + j
                rename = root + '/'+ i + '/' + rj
                shutil.move(origin , rename)
# Creates a gdb for Admin Units
def create_admin_gdb(d, l):
    #Creates a database to consolidate all the shp in a gdb
    gdb = "AdminUnits_" + l.upper()
    #Removes fgdb and shp folders
    if os.path.exists(gdb + ".gdb"):
        arcpy.Delete_management(root + "\\" + gdb + ".gdb")
        arcpy.CreateFileGDB_management(root, gdb)
        print("\n    Replacing Duplicate " + gdb + ".gdb\n")
    else:
        arcpy.CreateFileGDB_management(root, gdb)
        print("\n    Creating " + gdb + ".gdb\n")

    # copy the shp to gdb
    for path, subdirs, files in os.walk(root):
        for name in files:
            if name.endswith(".shp"):
                arcpy.CopyFeatures_management(root + "\\" + name[:-4] + "\\" + name , root + "\\"+ gdb + ".gdb\\" + name[:-4])
                print("    Importing " + name)
    # Delete folder, no longer needed
    for i in d['list']:
        if os.path.exists(i['file']+l):
            shutil.rmtree(root + '/' + i['file']+l)
# Changes the names of feature class to make updates easier
def create_lion_gdb(l):
    # moves the lion gdb
    shutil.move(root + "\\lion\\lion.gdb", root + "\\lion.gdb")
    shutil.rmtree(root + '/' + "lion")
    arcpy.env.workspace = root + "\\lion.gdb"
    old_line = "lion"
    new_line = "LION_" + l.upper()
    old_node = "node"
    new_node = "LION_NODE_" + l.upper()
    data_type = "FeatureClass"
    arcpy.Rename_management(old_line, new_line, data_type)
    arcpy.Rename_management(old_node, new_node, data_type)
    os.rename(root + "\\lion.gdb", root + "\\LION_" + l.upper() + ".gdb")

def zip_data(l):
    print("\n    Creating Zips\n")
    zipFileGeodatabase(root + "\\LION_" + l.upper() + ".gdb", root + "\\LION_" + l.upper() +".zip")
    zipFileGeodatabase(root + "\\AdminUnits_" + l.upper() +".gdb", root + "\\AdminUnits_" + l.upper() +".zip")

def zipFileGeodatabase(inFileGeodatabase, newZipFN):
   if not (os.path.exists(inFileGeodatabase)):
      return False

   if (os.path.exists(newZipFN)):
      os.remove(newZipFN)

   zipobj = zipfile.ZipFile(newZipFN,'w')

   for infile in glob.glob(inFileGeodatabase+"/*"):
      zipobj.write(infile, os.path.basename(inFileGeodatabase)+"/"+os.path.basename(infile), zipfile.ZIP_DEFLATED)

   zipobj.close()

   return True

def main():
    print(title)
    raw_lion = raw_input('    What is the latest version of LION? --> ')
    lion = raw_lion.lower()
    start = timeit.default_timer()
    manage_directories(data, lion)
    byting(data, lion)
    create_admin_gdb(data, lion)
    create_lion_gdb(lion)
    zip_data(lion)
    stop = timeit.default_timer()
    print("\n    Total Run Time: " +  str(stop - start) + " seconds")

if __name__ == '__main__':
    main()
