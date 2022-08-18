import pickle
import json
import numpy as np

Locations = None
Model = None

def get_estimated_price(location,sqft,bath,bal,bhk):
	try:
		loc_index = Locations.index(location.lower())
	except:
		loc_index = -1

	x = np.zeros(len(Locations)+4)
	x[0] = sqft
	x[1] = bath
	x[2] = bal
	x[3] = bhk
	if loc_index >= 0:
		x[loc_index+4] = 1

	return round(Model.predict([x])[0],2)

def load_locations():
	global Locations

	with open("../locations.json", "r") as f:
		Locations = json.load(f)['locations']

def load_model():
    global Model
    if Model is None:
        with open('../model.pickle', 'rb') as f:
            Model = pickle.load(f)
    print("Model Loading Done")

def get_location_names():
	return Locations


if __name__ == '__main__':
    
    load_locations()
    load_model()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000,1, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000,1, 2, 2))

