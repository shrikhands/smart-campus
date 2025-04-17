def safeguardLocationsGivenCrime():
    for location, crimes_type in session['prediction_values'].items():
        if (crime_selected == crimes_type):
            locations.append(location)
    return locations
    
