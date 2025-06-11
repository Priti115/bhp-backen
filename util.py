<<<<<<< HEAD
import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, BHK, bath):
    try:
        loc_index = __data_columns.index(location.lower()) if location.lower() in [loc.lower() for loc in __data_columns] else -1
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = BHK
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def get_location_names():
    global __locations
    print("Locations loaded in util.py:", __locations)  # Debugging line
    return __locations  # Returns list of locations

def load_saved_artifacts():
    print("Loading saved artifacts... start")
    global __data_columns
    global __locations
    global __model

    # Load column names
    with open("./artifacts/columns.json", 'r') as f:
        data = json.load(f)
        __data_columns = data['data_columns']
        __locations = __data_columns[3:]  # Location names start from index 3

    # Load model
    with open("./artifacts/banglore_home_price_model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("Loading saved artifacts... done")
    print("Available locations:", __locations)

if __name__ == '__main__':
    load_saved_artifacts()
    print("Testing location names:", get_location_names())
    print(get_estimated_price('Indira Nagar', 1000, 3, 3))
=======
import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, BHK, bath):
    try:
        loc_index = __data_columns.index(location.lower()) if location.lower() in [loc.lower() for loc in __data_columns] else -1
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = BHK
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def get_location_names():
    global __locations
    print("Locations loaded in util.py:", __locations)  # Debugging line
    return __locations  # Returns list of locations

def load_saved_artifacts():
    print("Loading saved artifacts... start")
    global __data_columns
    global __locations
    global __model

    # Load column names
    with open("./artifacts/columns.json", 'r') as f:
        data = json.load(f)
        __data_columns = data['data_columns']
        __locations = __data_columns[3:]  # Location names start from index 3

    # Load model
    with open("./artifacts/banglore_home_price_model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("Loading saved artifacts... done")
    print("Available locations:", __locations)

if __name__ == '__main__':
    load_saved_artifacts()
    print("Testing location names:", get_location_names())
    print(get_estimated_price('Indira Nagar', 1000, 3, 3))
>>>>>>> cc5d9b5e0842ff89bced500f8a7d139171c6fa73
