import csv

def importdatafromcsv (path):
    datalist = []
    with open(path, "r", encoding = "CP932") as f:
        reader = csv.reader(f)
        for row in reader:
            datalist.append(row)
    return datalist