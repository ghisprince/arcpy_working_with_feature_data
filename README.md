Short url to this repro: http://esriurl.com/10618

## Working with Feature Data Using ArcPy (demos)

This repo contains slides, as well as demos (python scripts and data) for the _Working with Feature Data Using ArcPy_ technical session.

This presentation was given at the Esri Developer Summit 2019 in Palm Springs.
 
## Prerequisite

 - ArcGIS - 10.2 or later 
 - Python 2.7.x

## Data
Costa Rica administrative boundaries can be downloaded from www.gadm.org (Global Administrative Areas site), click data by country, and then choose 
 - Country=Costa Rica
 - File format=ESRI file geodatabase

Costa Rica's canton is included in canton_pop.txt. The source of the data is the table "Cantons of Costa Rica" found at 
http://en.wikipedia.org/wiki/Cantons_of_Costa_Rica 
Included here under _Creative Commons Deed_ as per http://creativecommons.org/licenses/by-sa/3.0/

"US Census 2000 Case Study" Data Model used in demo3 is not included, it can be downloaded from http://downloads2.esri.com/support/TechArticles/Census.pdf, but i would recommend against it.  The mdb is verions 8.3 and seems to have problems (cannot be upgraded, cannot use arcpy.ListFeatureClasses on the feature dataset.  Just run the demo 3 code against your own data.

Once the data is downloaded run demos\demo_0_setup_data.py to setup for subsequent demos.
