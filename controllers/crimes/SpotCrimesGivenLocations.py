from models.Location import getLocationNum
from helpers.DateHelper import getDateObj, getWeekDay, getWeekNum, getMonth, getYear
from helpers.NumpyHelper import getNumpyArray
from helpers.PredictionHelper import getPrediction
from models.Crime import getCrimeType
from flask import jsonify

def spotCrimesEngine(data):
    # step1: encode prediction parameters
    location_num = getLocationNum(data.get('location'))
    date_obj = getDateObj(data.get('future-date'))
    week_num = getWeekNum(date_obj)
    week_day = getWeekDay(date_obj)
    month = getMonth(date_obj)
    time_hour = data.get('time-hour')
    year = getYear(date_obj)
    prediction_params = [location_num, week_num, week_day, month, time_hour, year]
    
    # step2: create numpy array
    numpy_arr = getNumpyArray(prediction_params)
    
    # step3: fetch prediction
    predicted_crime_num = getPrediction(numpy_arr)

    # step4: decode prediction
    crime_type = getCrimeType(predicted_crime_num)
    
    # step5: return json response
    return jsonify({"predicted-crime":crime_type})
