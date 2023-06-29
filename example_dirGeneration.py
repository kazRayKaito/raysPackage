import os
import random
import rayspackage as rp

rootdirpath = os.path.dirname(os.path.abspath(__file__))
dirpath = os.path.join(rootdirpath, "dir")
csvfilepath = os.path.join(dirpath, "numberList.csv")

fileNumber = 30
header = ["data", "data A", "data B", "data C"]

for fileIndex in range(fileNumber):
    filePath = os.path.join(dirpath, "data", f"data_{fileIndex + 1:03d}.csv")
    data = [header]
    for rowIndex in range(3):
        data.append([f"data_{rowIndex + 1}", random.random(), random.random(), random.random()])
    rp.file.saveAsCsv(filePath, data)