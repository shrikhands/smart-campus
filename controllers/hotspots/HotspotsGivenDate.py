from helpers.DateHelper import getDateObj, getWeekDay, getWeekNum, getMonth, getYear
from models.Location import getAllLocations
from helpers.NumpyHelper import getNumpyArray
from helpers.PredictionHelper import getPrediction, getPredictionProbabilities
from models.Crime import getCrimeType
from flask import jsonify

hotspots_with_probs = {}

def hotspotsEngine(data):
    # step1: encode prediction parameters
    #location_num = getLocationNum(data.get('location'))
    date_obj = getDateObj(data.get('future-date'))
    week_num = getWeekNum(date_obj)
    week_day = getWeekDay(date_obj)
    month = getMonth(date_obj)
    time_hour = data.get('time-hour')
    year = getYear(date_obj)
    
    hotspots = {}
    # loop over each location
    for location_num, location in getAllLocations().items():
        prediction_params = [location_num, week_num, week_day, month, time_hour, year]
        numpy_arr = getNumpyArray(prediction_params)
        predicted_crime_num = getPrediction(numpy_arr)
        predicted_probs = getPredictionProbabilities(numpy_arr)
        crime_type = getCrimeType(predicted_crime_num)
        hotspots[location] = crime_type
        hotspots_with_probs[location] = [crime_type, max(predicted_probs)]
        
    # return json object
    return jsonify(hotspots)

def getTopCrimeTypesWithProbs():
    type_frequency_with_probs = {}
    for location, crime_probs in hotspots_with_probs.items():
        crime_type = crime_probs[0]
        crime_prob = crime_probs[1]
        if (crime_type in type_frequency_with_probs):
            new_crime_prob = round((crime_prob + type_frequency_with_probs.get(crime_type))/2,2)
            type_frequency_with_probs[crime_type] = new_crime_prob
        else:
            type_frequency_with_probs[crime_type] = crime_prob
    return type_frequency_with_probs    
        
def getTopFiveCrimeTypes(data):
    type_frequency = {}
    for location, crime_type in data.items():
        if (crime_type in type_frequency):
            type_frequency[crime_type] += 1
        else:
            type_frequency[crime_type] = 1
    return type_frequency
