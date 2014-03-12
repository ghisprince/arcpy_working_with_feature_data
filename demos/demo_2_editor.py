"""

 arcpy.da.Editor doc
 http://resources.arcgis.com/en/help/main/10.2/index.html#/Editor/018w00000005000000/

 Fields toolset doc
 http://resources.arcgis.com/en/help/main/10.2/index.html#/An_overview_of_the_Fields_toolset/001700000046000000/

"""

import arcpy
import os

arcpy.env.workspace = os.getcwd() + "\\demo.gdb"
arcpy.DeleteField_management("canton", ["pop_per_km2", "provincia"])

arcpy.AddField_management("canton", "pop_per_km2", "DOUBLE")
arcpy.AddField_management("canton", "provincia", "TEXT", field_length=9)

####

arcpy.CalculateField_management("canton", "pop_per_km2", expression="!pop_2008! / !area_km2!", expression_type="PYTHON")
arcpy.CalculateField_management("canton", "provincia", expression="!NAME_1!", expression_type="PYTHON")

####

arcpy.DeleteField_management("canton", ["NAME_1"])


print("\nFINISHED")




####

def pprint_table(tab):
    """
     Pretty print of table's records
    """
    print("")
    def pprint(l):
        print(u"{:<10}\t{:<12}\t{:<10}\t{:<20}\t{:<10}\t{:<20}\t{:<12}\t{:<10}\t{:<12.2}\t{:<12}".format(*l))
    with arcpy.da.SearchCursor(tab, [i.name for i in arcpy.ListFields(tab) if (not 'Shape' in i.name)],) as cursor:
        pprint (cursor.fields)
        for row in cursor:
            pprint(row)


pprint_table("canton")

try:
    with arcpy.da.Editor(arcpy.env.workspace) as editor:
        arcpy.CalculateField_management("canton", "pop_per_km2", expression="!pop_2008! / !area_km2!", expression_type="PYTHON")
        pprint_table("canton")
        arcpy.CalculateField_management("canton", "provincia", expression="!NAME_1!", expression_type="PYTHON")
except arcpy.ExecuteError as e:
    print(e)

pprint_table("canton")