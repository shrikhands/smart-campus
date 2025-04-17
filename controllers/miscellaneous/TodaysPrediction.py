from helpers.DateHelper import getTodaysDateObj, getWeekNum, getWeekDay, getMonth, getYear
from helpers.NumpyHelper import getNumpyArray
from helpers.PredictionHelper import getTodaysModelPrediction
from flask import jsonify
from models.Crime import getCrimeType
from models.Location import getLocationName

def getTodaysPrediction(todays_date):
    # encode date values to pass
    date_obj = getTodaysDateObj(todays_date)
    week_num = getWeekNum(date_obj)
    week_day = getWeekDay(date_obj)
    month = getMonth(date_obj)
    year = getYear(date_obj)
    
    # create numpy array for prediction
    prediction_params = [week_num, week_day, month, 0, year]
    numpy_arr = getNumpyArray(prediction_params)
    
    # call predict of model
    multi_pred_values = getTodaysModelPrediction(numpy_arr)
    
    # decode the crime_type and location_name
    response_values = {}
    response_values["crime_type"] = getCrimeType(round(multi_pred_values[0]))
    response_values["location_name"] = getLocationName(round(multi_pred_values[1]))
    
    # return json response
    return jsonify(response_values)