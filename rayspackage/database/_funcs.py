def getKeys(data):
    return data[0]

def transpose(data):
    transposedData = []
    for i in range(len(data[0])):
        newrow = []
        for row in data:
            newrow.append(row[i])
        transposedData.append(newrow)
    return transposedData

def flattenData(data, transposeDo = False):
    if transposeDo:
        #data = transpose(data)
        data = transpose(data)
    flattenData = []
    flattenHead = []
    rowHeaderList = data[0][1:]
    for row in data[1:]:
        columnHead = row[0]
        for column, rowHeader in zip(row[1:], rowHeaderList):
            flattenHead.append(f"[{columnHead}] [{rowHeader}]")
            flattenData.append(column)
    return [flattenHead, flattenData]

def flattenDataT(data):
    data = transpose(data)
    flattenData = []
    flattenHead = []
    rowHeaderList = data[0][1:]
    for row in data[1:]:
        columnHead = row[0]
        for column, rowHeader in zip(row[1:], rowHeaderList):
            flattenHead.append(f"[{rowHeader}] [{columnHead}]")
            flattenData.append(column)
    return [flattenHead, flattenData]