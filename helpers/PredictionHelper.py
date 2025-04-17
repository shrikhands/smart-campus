import pickle
model = pickle.load(open('knn_model.pkl', 'rb'))
model_lr = pickle.load(open('lr_model.pkl', 'rb'))
internal_data = {}
top_crimes = {}

def getPredictionProbabilities(numpy_arr):
    return model.predict_proba(numpy_arr)[0]  

def getPrediction(numpy_arr):
    return model.predict(numpy_arr)[0]

def setPredictionText(data):
    internal_data = data
    
def getPredictionText():
    return internal_data
    
def returnPredictionText():
    return internal_data

def getTodaysModelPrediction(numpy_arr):
    return model_lr.predict(numpy_arr)[0]

def getPredictionTopCrimeTypes():
    return top_crimes

def getLatLngsDict():
    return []