def getStart():
    with open('./8332BDS.txt', 'r') as f:
        start = f.readline()
        data = start.split()
        startstp = data[0]
    return startstp

def getEnd():
    with open('./8332BDS.txt', 'r') as f:
        print(len(f))
        
getEnd()