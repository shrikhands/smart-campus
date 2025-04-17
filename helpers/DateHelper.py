import datetime
#from dateutil import parser

def getDateObj(future_date):
    #print("future_date : ",parser.parse(future_date))
    return datetime.datetime.strptime(future_date, '%Y-%m-%d')

def getWeekNum(d):
    return d.isocalendar()[1]

def getWeekDay(d):
    return d.isocalendar()[2]

def getMonth(d):
    return d.month

def getYear(d):
    return d.isocalendar()[0]

def getTodaysDate():
    return datetime.datetime.today().strftime("%B %d, %Y")

def getTodaysDateObj(todays_date):
    return datetime.datetime.strptime(todays_date, '%B %d, %Y')
