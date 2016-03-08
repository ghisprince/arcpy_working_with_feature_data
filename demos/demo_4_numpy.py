"""
 Working with NumPy in ArcGIS Doc
 http://desktop.arcgis.com/en/arcmap/latest/analyze/python/working-with-numpy-in-arcgis.htm

 has links to doc for: TableToNumPyArray, NumPyArrayToTable, ExtendTable,
                       RasterToNumPyArray, NumPyArrayToRaster

"""

import arcpy
import os

arcpy.env.workspace = os.getcwd() + "\\demo.gdb"

# TableToNumPyArray signature is much like da.SearchCursor
arr = arcpy.da.TableToNumPyArray("canton", "pop_2008")

print(arr)
print(arr.dtype)

print("\n")
print("Costa Rica canton population facts")
print("Sum : {:,}".format(arr['pop_2008'].sum()))
print("Std : {:.1}".format(arr['pop_2008'].std()))
print("Min : {}".format(arr['pop_2008'].min()))
print("Max : {}".format(arr['pop_2008'].max()))

arr = arcpy.da.TableToNumPyArray("canton", ("canton", "provincia", "area_km2", "pop_2008",))

print(arr)
print(arr.dtype)

print("{:.2} people/km2".format(arr['pop_2008'].sum() / arr['area_km2'].sum()))

import pandas as pd
df = pd.DataFrame(arr,)
print(df.columns)
print(df.sort('pop_2008', ascending=False).head())

print(df.groupby('provincia').sum())

print ("\nFINISHED")
