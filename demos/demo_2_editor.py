"""

 arcpy.da.Editor doc
 http://resources.arcgis.com/en/help/main/10.2/index.html#/Editor/018w00000005000000/

 Fields toolset doc
 http://resources.arcgis.com/en/help/main/10.2/index.html#/An_overview_of_the_Fields_toolset/001700000046000000/

"""

import arcpy
import os

def pprint_table(tab):
    """
     Pretty print of table's records
    """
    print("")
    def pprint(l):
        print("{:<12}\t{:<10}\t{:<12}\t{:<12}".format(*l))

    with arcpy.da.SearchCursor(tab, field_names = ('OID', 'Canton', 'pop_2008', 'area_km2_geod', 'pop_per_km2'),
                               ) as cursor:
        pprint (cursor.fields)
        for row in cursor:
            pprint(row)



arcpy.env.workspace = os.getcwd() + "\\demo.gdb"
arcpy.DeleteField_management("canton", ["area_km2_geod", "pop_per_km2"])
arcpy.AddField_management("canton", "area_km2_geod", "DOUBLE")
arcpy.AddField_management("canton", "pop_per_km2", "DOUBLE")

pprint_table("canton")

try:
    with arcpy.da.Editor(arcpy.env.workspace) as editor:
        arcpy.CalculateField_management("canton", "area_km2_geod", expression="!shape.geodesicArea@SQUAREKILOMETERS!", expression_type="PYTHON")
        pprint_table("canton")
        arcpy.CalculateField_management("canton", "pop_per_km2", expression="!pop_2008! / !area_km2!")
        resize_field()
except arcpy.ExecuteError as e:
    print(e)

pprint_table("canton")

print("\nFINISHED")