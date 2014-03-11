"""
 arcpy.da.Walk Doc
 http://resources.arcgis.com/en/help/main/10.2/index.html#/Walk/018w00000023000000/

 arcpy.da.ListDomains doc
 http://resources.arcgis.com/en/help/main/10.2/index.html#/ListDomains/018w0000001z000000/

"""

import arcpy
import os


def pprint_domain(domain):
    """
    Pretty prints a gdb domain
    """
    print("Domain name : {}".format(domain.name))
    print("Domain type : {}".format(domain.type))
    if domain.domainType == "CodedValue":
        coded_values = domain.codedValues
        for k, v in coded_values.iteritems():
            print("{} : {}".format(k, v))
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

from pprint import pprint
for dirpath, dirnames, filenames in arcpy.da.Walk(os.getcwd(), datatype="FeatureClass"):
    for filename in filenames:
        fc = os.path.join(dirpath, filename)
        st = arcpy.da.ListSubtypes(fc)
        if len(st.keys()) > 1:
            pprint(st)

print ("\nFINISHED")
