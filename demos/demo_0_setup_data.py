import arcpy
import os

arcpy.env.overwriteOutput = True
arcpy.env.workspace = os.path.dirname(__file__)

if not arcpy.Exists(os.getcwd() + "\\demo.gdb"):
    arcpy.CreateFileGDB_management(os.getcwd(), "demo.gdb")

# Load data
arcpy.Copy_management(r"CRI_adm.gdb\CRI_adm2", r"demo.gdb\canton")
arcpy.TableToTable_conversion("canton_pop.txt", os.getcwd() + "\\demo.gdb",
                              "canton_pop", field_mapping="""Canton "Canton" true true false 255 Text 0 0 ,First,#,canton_pop.txt,Canton,-1,-1;area_km2 "area_km2" true true false 8 Double 0 0 ,First,#,canton_pop.txt,Area (km2),-1,-1;pop_2008 "pop_2008" true true false 4 Long 0 0 ,First,#,canton_pop.txt,Pop. (2008),-1,-1""", config_keyword="")

# Delete cruft
arcpy.DeleteField_management(r"demo.gdb\canton", ['NAME_0', 'ID_0', 'ID_1',
                                                  'ID_2', 'NL_NAME_2',
                                                  'VARNAME_2', 'ENGTYPE_2',
                                                  'TYPE_2', 'ISO'],)


# Join two datasets (canton population to canton polys)
arcpy.JoinField_management(r"demo.gdb\canton", "NAME_2",
                           r"demo.gdb\canton_pop", "Canton")

print ("\nFINISHED")
