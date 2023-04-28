import datetime

def getTimeinterval(date1):
    date2 = '2006 01 01 00 00 00'

    d1 = datetime.datetime.strptime(date1, '%Y %m %d %H %M %S')
    d2 = datetime.datetime.strptime(date2, '%Y %m %d %H %M %S')

    d = d1 - d2

    timeinterval = int(d.days * 24 * 3600) + int(d.seconds)

    bdsWeek = timeinterval // (7*24*3600)
    bdsSecond = timeinterval % (7*24*3600)
    
    return bdsWeek, bdsSecond