crime_types = {1:'disturbing the peace',
                   2:'theft',
                   3:'hit and run',
                   4:'other agency misdemeanor warrant',
                   5:'driving under influence of drugs/alcohol',
                   6:'vandalism',
                   7:'assault/sexual/battery report',
                   8:'possession of controlled substance/marijuana or public drunkenness',
                   9:'burglary',
                   10:'motor vehicle theft/report of lost or stolen license plate'}

def getCrimeType(crime_num):
    return crime_types.get(crime_num)
