import csv

def importdatafromcsv (path):
    datalist = []
    with open(path, "r", encoding = "CP932") as f:
        reader = csv.reader(f)
        for row in reader:
            datalist.append(row)
    return datalist

def saveAsCsv(path, data):
    with open(path, "w", encoding = "CP932", newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)