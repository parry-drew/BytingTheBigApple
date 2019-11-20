#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# BytingTheBigApple.py
# This script will download LION and Amdin Shapefiles from DCP's Bytes of The
# Big Apple Page.
#
# C:\Python27\ArcGIS10.7\python.exe BytingTheBigApple.py
#
# ---------------------------------------------------------------------------
import os, json, csv, datetime, timeit, time, urllib2, shutil, zipfile, arcpy, glob, webbrowser
from zipfile import *
from arcpy import env

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
   "lion_list":[
      {
         "file":"nyad",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyad_",
         "name":"State_Assembly_Districts",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nyadwi",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyadwi_",
         "name":"State_Assembly_Districts_Water_Area_Included",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nybb",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nybb_",
         "name":"Borough_Boundary",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nybbwi",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nybbwi_",
         "name":"Borough_Boundary_Water_Area_Included",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nycc",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycc_",
         "name":"City_Council_Districts",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nyccwi",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyccwi_",
         "name":"City_Council_Districts_Water_Area_Included",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nycd",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycd_",
         "name":"Community_Districts",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nycdwi",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycdwi_",
         "name":"Community_Districts_Water_Area_Included",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nycgwi",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycgwi_",
         "name":"US_Congressional_Districts_Water_Area_Included",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nycg",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycg_",
         "name":"US_Congressional_Districts",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nyed",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyed_",
         "name":"Election_Districts",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nyedwi",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyedwi_",
         "name":"Election_Districts_Water_Area_Included",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nyfb",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyfb_",
         "name":"Fire_Battalions",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nyfc",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyfc_",
         "name":"Fire_Companies",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nyfd",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyfd_",
         "name":"Fire_Divisions",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nyha",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyha_",
         "name":"Health_Area",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nyhc",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyhc_",
         "name":"Health_Centers",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nymc",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nymc_",
         "name":"Municipal_Court_Districts",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nymcwi",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nymcwi_",
         "name":"Municipal_Court_Districts_Water_Area_Included",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nypp",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nypp_",
         "name":"Police_Precincts",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nysd",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nysd_",
         "name":"School_Districts",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nyss",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyss_",
         "name":"State_Senate_Districts",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nysswi",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nysswi_",
         "name":"State_Senate_Districts_Water_Area_Included",
         "gisgrid":"BOUNDARIES"
      },
      {
         "file":"nycb2000",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycb2000_",
         "name":"Census_Blocks_2000",
         "gisgrid":"CENSUS"
      },
      {
         "file":"nycb2000wi",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycb2000wi_",
         "name":"Census_Blocks_2000_Water_Area_Included",
         "gisgrid":"CENSUS"
      },
      {
         "file":"nycb2010",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycb2010_",
         "name":"Census_Blocks_2010",
          "gisgrid":"CENSUS"
      },
      {
         "file":"nycb2010wi",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycb2010wi_",
         "name":"Census_Blocks_2010_Water_Area_Included",
          "gisgrid":"CENSUS"
      },
      {
         "file":"nyct2000",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyct2000_",
         "name":"Census_Tracts_2000",
         "gisgrid":"CENSUS"
      },
      {
         "file":"nyct2000wi",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyct2000wi_",
         "name":"Census_Tracts_2000_Water_Area_Included",
         "gisgrid":"CENSUS"
      },
      {
         "file":"nyct2010",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyct2010_",
         "name":"Census_Tracts_2010",
         "gisgrid":"CENSUS"
      },
      {
         "file":"nyct2010wi",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyct2010wi_",
         "name":"Census_Tracts_2010_Water_Area_Included",
         "gisgrid":"CENSUS"
      },
      {
         "file":"nyclion",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyclion_",
         "name":"LION",
         "gisgrid":"LION"
      },
      {
         "file":"nyap",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyap_",
         "name":"ATOMIC_POLYGON",
         "gisgrid":"LION"
      },
      {
         "file":"nynta",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nynta_",
         "name":"Neighborhood_Tabulation_Areas",
         "gisgrid":"CENSUS"
      },
      {
         "file":"nypuma",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nypuma_",
         "name":"PUMA",
         "gisgrid":"CENSUS"
      },
      {
         "file":"nyhez",
         "url":"https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyhez_",
         "name":"Hurricane_Evacuation_Zones",
         "gisgrid":"PUBLICSAFETY"
      },

   ]
}



# Clears out old folder.
def manage_directories(d, l):
    #creates or replaces drectories
    for i in d['lion_list']:
        if os.path.exists(i['file']+l):
            shutil.rmtree(root + '/' + i['file']+l)

    for i in glob.glob("*.gdb"):
        shutil.rmtree(i)

    for i in glob.glob("*.zip"):
        shutil.rmtree(i)
# Gathers data from Bytes of The Big Apple and Unzips it. Also makes the LION gdb
def byting(d, l):
    #used to over come proxy issue in the office
    proxy = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)

    for i in d['lion_list']:
        try:
            f = urllib2.urlopen(i['url'] + l + '.zip')
            data = f.read()
            with open(i['file']+ l + ".zip", "wb") as code:
                code.write(data)

            with zipfile.ZipFile(root + '/' + i['file'] + l.upper() + '.zip', "r") as z:
                z.extractall(root)

            print("    " + i['file'] + l + " Downloaded and Unzipped")
            os.remove(i['file'] + l + ".zip")
        except urllib2.HTTPError:
            pass
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
                arcpy.CopyFeatures_management(path + "\\" + name , root + "\\"+ gdb + ".gdb\\" + name[:-4])
                print("    Importing " + name)
    # Delete folder, no longer needed
    for i in d['lion_list']:
        if os.path.exists(i['file'] + "_" + l):
            shutil.rmtree(root + '/' + i['file'] + "_" + l)
# Changes the names of feature class to make updates easier
def create_lion_gdb(l):
    # moves the lion gdb
    shutil.move(root + "\\lion\\lion.gdb", root + "\\lion.gdb")
    shutil.rmtree(root + '/' + "lion")
    arcpy.env.workspace = root + "\\lion.gdb"
    arcpy.Rename_management("lion", "LION_", "FeatureClass")
    arcpy.Rename_management("LION_", "LION", "FeatureClass")
    arcpy.Rename_management("node", "NODE_", "FeatureClass")
    arcpy.Rename_management("NODE_", "LION_NODE", "FeatureClass")
    time.sleep(10)
    os.rename(root + "\\lion.gdb", root + "\\LION_" + l.upper() + ".gdb")

def rename_features(d,l):
    try:
        env.workspace = root + "\\AdminUnits_" + l.upper() + ".gdb"
        for i in d['lion_list']:
            if i['file'] != "nyclion":
                print("    " + i['file'] + " renamed")
                arcpy.Rename_management(i['file'], i['name'])
    except:
        print("    " + i['file'] + " was not found or had an error.")

def zip_data(l):
    print("\n    Creating Zips\n")
    zipFileGeodatabase(root + "\\LION_" + l.upper() + ".gdb", root + "\\LION_" + l.upper() +".zip")
    zipFileGeodatabase(root + "\\AdminUnits_" + l.upper() +".gdb", root + "\\AdminUnits_" + l.upper() +".zip")
    zipFileGeodatabase(root + "\\Other.gdb", root + "\\Other.zip")

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

def cleanUp():
    print('    Cleaning Up The Directory')
    for pdf in glob.glob("*.pdf"):
        os.remove(pdf)
    for html in glob.glob("*.html"):
        os.remove(html)

def main():
    print(title)
    raw_lion = raw_input('    What is the latest version of LION? --> ')
    lion = raw_lion.lower()
    start = timeit.default_timer()
    manage_directories(data, lion)
    byting(data, lion)
    create_admin_gdb(data, lion)
    rename_features(data, lion)
    create_lion_gdb(lion)
    zip_data(lion)
    cleanUp()
    webbrowser.open('http://cityshare.nycnet/html/gis/html/downloads/downloads.shtml#3d')
    webbrowser.open('https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-pluto-mappluto.page')
    webbrowser.open('https://data.cityofnewyork.us/Housing-Development/Scenic-Landmarks/gi7d-8gt5')
    webbrowser.open('https://data.cityofnewyork.us/Transportation/Subway-Entrances/drex-xx56')
    webbrowser.open('https://data.cityofnewyork.us/Housing-Development/Map-of-NYCHA-Developments/i9rv-hdr5')
    stop = timeit.default_timer()
    print("\n    Total Run Time: " +  str(stop - start) + " seconds")
    print("\n    Add the following features manually :^)")
    print("\n    MapPluto,")
    print("\n    Buildings,")
    print("\n    Historic Dtricts,")
    print("\n    Scenic Landmarks,")
    print("\n    Subway Entrances,")
    print("\n    See the Bytes of the Big Apple Repo for more info :")
    print("\n    http......")

if __name__ == '__main__':
    main()
