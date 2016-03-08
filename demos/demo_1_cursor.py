"""

 arcpy.da.SearchCursor doc
 http://desktop.arcgis.com/en/arcmap/latest/analyze/arcpy-data-access/searchcursor-class.htm

 arcpy.da.UpdateCursor doc
 http://desktop.arcgis.com/en/arcmap/latest/analyze/arcpy-data-access/updatecursor-class.htm

"""

import arcpy
import os

arcpy.env.workspace = os.getcwd() + "\\demo.gdb"

with arcpy.da.SearchCursor("canton", "*") as cursor:
    for row in cursor:
        print (row)


# List canton with no pop
with arcpy.da.SearchCursor("canton", ("NAME_2", "pop_2008"), "pop_2008 IS NULL") as cursor:
    for row in cursor:
        print (row[0])


# Now let's find difference
with arcpy.da.SearchCursor("canton", "NAME_2") as cursor:
    fc = [row[0] for row in cursor]


with arcpy.da.SearchCursor("canton_pop", "Canton") as cursor:
    tab = [row[0] for row in cursor]


print("\nCANTONS IN FC NOT IN TABLE")
for i in list(set(fc) - set(tab)):
    print(i)


print("\nCANTONS IN TABLE NOT IN FC")
for i in list(set(tab) - set(fc)):
    print(i)


lookup = {u'Le\xf3n Cort\xe9s'      : u'Le\xf3n Cort\xe9s Castro',
          u'V\xe1squez de Coronado' : u'V\xe1zquez de Coronado' }


with arcpy.da.UpdateCursor("canton",
                           field_names = ("NAME_2", "Canton", "area_km2","pop_2008"),
                           where_clause = u"NAME_2 IN ('Le\xf3n Cort\xe9s', 'V\xe1squez de Coronado') ") as fc_cursor:
    for fc_row in fc_cursor:
        with arcpy.da.SearchCursor("canton_pop",
                                   field_names = ("Canton", "area_km2","pop_2008"),
                                   where_clause = u"Canton = '{}'".format(lookup[fc_row[0]])) as tab_cursor:
            for tab_row in tab_cursor:
                print("fc_row  : {}".format(fc_row))
                print("tab_row : {}".format(tab_row))
                fc_cursor.updateRow(fc_row[:1] + list(tab_row))


print ("\nFINISHED")
