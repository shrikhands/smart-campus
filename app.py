from flask import Flask, request, jsonify, render_template, session
from controllers.crimes.SpotCrimesGivenLocations import spotCrimesEngine
from controllers.hotspots.HotspotsGivenDate import hotspotsEngine, getTopFiveCrimeTypes, getTopCrimeTypesWithProbs
from helpers.PredictionHelper import setPredictionText, getLatLngsDict
from helpers.DateHelper import getTodaysDate
from controllers.miscellaneous.TodaysPrediction import getTodaysPrediction
from controllers.locations.SafeguardLocationsGivenCrime import safeguardLocationsGivenCrime
from controllers.miscellaneous.ReportLog import saveReport

# constructor
app = Flask(__name__) #Initializing the flask App
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' #this can be set to any other key of your choice

@app.route('/')
def home():
    multi_preds_json = getTodaysPrediction(getTodaysDate())
    todays_crime = multi_preds_json.json.get('crime_type')
    todays_location = multi_preds_json.json.get('location_name')
    session['todays_crime'] = todays_crime
    session['todays_location'] = todays_location
    return render_template('main.html', todays_date = getTodaysDate(), todays_crime = todays_crime.capitalize(), todays_location = todays_location.capitalize())

@app.route('/spotcrimes', methods=['GET', 'POST'])
def spotcrimes():
    json_request = jsonify(request.form)
    json_resp = spotCrimesEngine(json_request.json)
    prediction_text = json_resp.json.get('predicted-crime')
    return render_template('main.html', prediction_text = prediction_text)

@app.route('/safeguardlocations', methods=['GET', 'POST'])
def safeguardlocations():
    return render_template('main.html')

"""
@app.route('/getmap/<crime_selected>/', methods=['GET', 'POST'])
def getmap(crime_selected):
    # part1: get locations
    locations = safeguardLocationsGivenCrime(crime_selected)
    
    # part2: get the corresponding lat-lngs
    markers = getLatLngsDict(locations)
    
    hotspots_map = Map(
        markers=[(marker[0], marker[1]) for marker in markers],
        fit_markers_to_bounds = True
    )
    return render_template('main.html', custom_map = hotspots_map)
"""

@app.route('/reportcrime', methods=['GET', 'POST'])
def reportcrime():
    saveReport = jsonify(request.form).json
    return render_template('main.html')

@app.route('/get_session', methods = ['GET', 'POST'])
def get_session():
    return jsonify(session['prediction_values'])

@app.route('/hotspots', methods=['GET', 'POST'])
def hotspots():
    json_request = jsonify(request.form)
    json_resp = hotspotsEngine(json_request.json)
    session['prediction_values'] = json_resp.json
    setPredictionText(json_resp.json)
    prediction_top_crime_types = getTopFiveCrimeTypes(json_resp.json)
    top_crime_types_with_probs = [getTopCrimeTypesWithProbs()]
    print("top_crime_types_with_probs: ",top_crime_types_with_probs)
    session['top_crimes'] = prediction_top_crime_types
    prediction_text = spotCrimesEngine(json_request.json)
    
    setPredictionText(prediction_text.json)
    prediction_text = prediction_text.json.get('predicted-crime')
    return render_template('main.html', prediction_top_crime_types = prediction_top_crime_types, 
                                        prediction_crime = prediction_text, 
                                        given_location = json_request.json.get('location'), 
                                        given_date = json_request.json.get('future-date'),
                                        given_time = json_request.json.get('time-hour'),
                                        todays_date = getTodaysDate(),
                                        todays_crime = session['todays_crime'].capitalize(),
                                        todays_location = session['todays_location'],
                                        top_crime_types_with_probs = top_crime_types_with_probs)
    
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8080) #un-comment this line and comment the line below when updating file on cloud-server
    app.run(debug = True, use_reloader = False)