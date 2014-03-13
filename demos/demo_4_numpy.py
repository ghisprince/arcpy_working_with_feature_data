"""
 Working with NumPy in ArcGIS Doc
 http://resources.arcgis.com/en/help/main/10.2/index.html#//002z00000028000000

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
print("Min : {}".format(arr['pop_2008'].max()))

arr = arcpy.da.TableToNumPyArray("canton", ("canton", "area_km2", "pop_2008",))

print(arr)
print(arr.dtype)

print ("\nFINISHED")