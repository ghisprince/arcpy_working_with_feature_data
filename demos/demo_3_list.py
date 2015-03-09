"""
 arcpy.da.Walk Doc
 

 arcpy.da.ListDomains doc
 http://desktop.arcgis.com/en/desktop/latest/analyze/arcpy-data-access/walk.htm

"""

import arcpy
import os


def pprint_domain(domain):
    """
    Pretty prints a gdb domain
    """
    print("")
    print("Domain name      : {}".format(domain.name))
    print("Domain type      : {}".format(domain.domainType))
    print("Domain FieldType : {}".format(domain.type))
    if domain.domainType == "CodedValue":
        coded_values = domain.codedValues
        print("Coded Values")
        for k, v in coded_values.iteritems():
            print("{}, {}".format(k, v))
    elif domain.domainType == "Range":
        print("Min: {}".format(domain.range[0]))
        print("Max: {}".format(domain.range[1]))



print("arcpy da walk")
for dirpath, dirnames, filenames in arcpy.da.Walk(os.getcwd(), datatype="FeatureClass"):
    for filename in filenames:
        print(os.path.join(dirpath, filename))



print("os walk")
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if ".mdb" in filename:
            mdb = os.path.join(dirpath, filename)
            print(mdb)
            for domain in arcpy.da.ListDomains(mdb):
                pprint_domain(domain)

arcpy.env.workspace = os.path.join(os.path.join(os.getcwd(), r"Census2000CaseStudy\Census 2000 schema.gdb\Census2000DataSample"))


for fc in arcpy.ListFeatureClasses():
    for f in arcpy.ListFields(fc):
        if f.domain:
            print("fc={}, field={}, domain={}".format(fc, f.name, f.domain))

from pprint import pprint
for dirpath, dirnames, filenames in arcpy.da.Walk(os.getcwd(), datatype="FeatureClass"):
    for filename in filenames:
        fc = os.path.join(dirpath, filename)
        st = arcpy.da.ListSubtypes(fc)
        if len(st.keys()) > 1:
            pprint(st)

print ("\nFINISHED")