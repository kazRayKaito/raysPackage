import os
import random
import rayspackage as rp

rootdirpath = os.path.dirname(os.path.abspath(__file__))
dirpath = os.path.join(rootdirpath, "dir")
datapath = os.path.join(dirpath, "data")
fileList = os.listdir(datapath)

data = []
header = []

for file in fileList:
    #Open each file
    filepath = os.path.join(datapath, file)
    filedata = rp.file.importdatafromcsv(filepath)

    #Process Data
    [flatHead, flatData] = rp.database.flattenData(filedata, True)

    #Save head
    if len(data) == 0:
        data.append(["fileName"] + flatHead)
    
    #Save data
    data.append([file] + flatData)

savepath = os.path.join(dirpath, "data.csv")
rp.file.saveAsCsv(savepath, data)