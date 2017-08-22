BytingTheBigApple.py
======

The purpose of this script is automate the process of gather administrative boundaries and LION from
DCP's [Bytes of The Big Apple](http://www1.nyc.gov/site/planning/data-maps/open-data.page) using ArcPy.

## Directions
1. In the command line change directory to the location of the BytingTheBigApple.py

```
    cd Your\Directory\BytingTheBigApple.py
```

2. Run the script as seen below. The example below is a very basic. The first half is call the python.exe location. The second half is the Python script.

```
    C:\Python27\ArcGIS10.4\python.exe BytingTheBigApple.py
```

3. When prompted,  type in the three digit code for the latest version of LION and then press enter.For example "17A".

4. After the script has completed you should have two zip files and two gdb containing admin units and lion in the same directory.

##  Tips
1. The JSON that lists all the dataset makes an assuption about how you name your database connections in ArcCatalog. So if you are having issues you may need to rename these connections either in the code or ArcCatalog.

2. Technically you can use this script to obtain previous versions of LION by putting in the three digit code from an older version.
