
## Working with Feature Data Using ArcPy (demos)

This repo contains demos (python scripts) and data for the _Working with Feature Data Using ArcPy_ technical session.

This presentation was given at the Esri Developer Summit 2014 & 2015 in Palm Springs.
 
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

## Licensing
Copyright 2014 Esri

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

A copy of the license is available in the repository's [license.txt](license.txt) file.
