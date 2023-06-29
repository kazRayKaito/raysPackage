import os
import rayspackage as rp

rootdirpath = os.path.dirname(os.path.abspath(__file__))
dirpath = os.path.join(rootdirpath, "dir")
csvfilepath = os.path.join(dirpath, "dirlist.csv")

datalines = rp.file.importdatafromcsv(csvfilepath)

for dataline in datalines:
    print(dataline)

print(rp.database.getKeys(datalines))