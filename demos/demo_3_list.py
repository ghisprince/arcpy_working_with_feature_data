"""
 arcpy.da.Walk Doc
 http://desktop.arcgis.com/en/arcmap/latest/analyze/arcpy-data-access/walk.htm

 arcpy.da.ListDomains doc
 http://desktop.arcgis.com/en/arcmap/latest/analyze/arcpy-data-access/listdomains.htm

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

print("="*80)
cwd = os.getcwd()
print("current working dir: " + cwd)

# Using arcpy.da.Walk
print("arcpy da walk")
for dirpath, dirnames, filenames in arcpy.da.Walk(cwd, datatype="FeatureClass"):
    print(dirpath)
    for filename in filenames:
        print(" - " + filename)


# Using os.walk and arcpy.da.ListDomains
print("="*80)
print("os walk and listDomain")
for dirpath, dirnames, filenames in os.walk(cwd):
    for filename in filenames:
        if ".mdb" in filename:
            mdb = os.path.join(dirpath, filename)
            print(mdb)
            for domain in arcpy.da.ListDomains(mdb):
                pprint_domain(domain)


# Using ListFeatureClasses and ListFields
arcpy.env.workspace = os.path.join(cwd, r"Census2000CaseStudy\Census 2000 schema.gdb\Census2000DataSample")

for fc in arcpy.ListFeatureClasses():
    for f in arcpy.ListFields(fc):
        if f.domain:
            print("fc={}, field={}, domain={}".format(fc, f.name, f.domain))


# Using arcpy.da.ListSubtypes
print("="*80)
from pprint import pprint
for dirpath, dirnames, filenames in arcpy.da.Walk(cwd, datatype="FeatureClass"):
    for filename in filenames:
        fc = os.path.join(dirpath, filename)
        st = arcpy.da.ListSubtypes(fc)
        if len(st.keys()) > 1:
            pprint(st)

print ("\nFINISHED")
