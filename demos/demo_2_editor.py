"""

 arcpy.da.Editor doc
 http://desktop.arcgis.com/en/arcmap/latest/analyze/arcpy-data-access/editor.htm

 Fields toolset doc
 http://desktop.arcgis.com/en/arcmap/latest/tools/data-management-toolbox/an-overview-of-the-fields-toolset.htm


"""

import arcpy
import os

arcpy.env.workspace = os.getcwd() + "\\demo.gdb"
arcpy.DeleteField_management("canton", ["pop_per_km2", "provincia"])

arcpy.AddField_management("canton", "pop_per_km2", "DOUBLE")
arcpy.AddField_management("canton", "provincia", "TEXT", field_length=9)

####
arcpy.CalculateField_management("canton", "area_km2", expression="!shape.geodesicArea@SQUAREKILOMETERS!", expression_type="PYTHON")
arcpy.CalculateField_management("canton", "pop_per_km2", expression="!pop_2008! / !area_km2!", expression_type="PYTHON")
arcpy.CalculateField_management("canton", "provincia", expression="!NAME_1!", expression_type="PYTHON")

####

print("\nFINISHED")


####

def pprint_table(tab):
    """
     Pretty print of table's records
    """
    print("-"*80)
    def pprint(l):
        print(u"{:<10}\t{:<20}\t{:<20}\t{:<20}".format(*l))
    with arcpy.da.SearchCursor(tab, ['ObjectID', 'NAME_1', "provincia", 'pop_per_km2'],) as cursor:
        pprint (cursor.fields)
        for row in cursor:
            pprint(row)


pprint_table("canton")

try:
    with arcpy.da.Editor(arcpy.env.workspace) as editor:
        arcpy.CalculateField_management("canton", "area_km2", expression="!shape.geodesicArea@SQUAREKILOMETERS!", expression_type="PYTHON")
        arcpy.CalculateField_management("canton", "pop_per_km2", expression="!pop_2008! / !area_km2!", expression_type="PYTHON")
        pprint_table("canton")
        arcpy.CalculateField_management("canton", "provincia", expression="!NAME_1!", expression_type="PYTHON")
except arcpy.ExecuteError as e:
    print(e)

pprint_table("canton")

####
