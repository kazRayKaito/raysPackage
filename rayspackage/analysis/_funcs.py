import statistics

def getStdevS(list):
    data = []
    for item in list:
        data.append(float(item))
    return statistics.stdev(data)

def getStdevP(list):
    data = []
    for item in list:
        data.append(float(item))
    return statistics.pstdev(data)