from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import util
import os

# Setup Flask to serve static files from the client folder
app = Flask(__name__, static_folder='../client', static_url_path='')
CORS(app)

# Load model and other artifacts
print("Initializing model...")
util.load_saved_artifacts()
print("Model initialized.")

# Serve index.html as home page
@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

# Serve static files like app.js, app.css
@app.route('/<path:path>')
def static_file(path):
    return send_from_directory(app.static_folder, path)

# API to get location names
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    locations = util.get_location_names()
    response = jsonify({'locations': locations})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# API to predict price
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        BHK = int(request.form['BHK'])
        bath = int(request.form['bath'])

        estimated_price = util.get_estimated_price(location, total_sqft, BHK, bath)

        response = jsonify({'estimated_price': estimated_price})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    print("Flask is running, Priti! 🚀")
     app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))



