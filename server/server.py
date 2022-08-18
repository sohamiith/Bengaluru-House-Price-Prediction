from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/list_locations', methods=['GET'])
def list_locations():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_house_price', methods=['GET', 'POST'])
def predict_house_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    bal = int(request.form['bal'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bath,bal,bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    
    util.load_locations()
    print("location loadded")
    util.load_model()
    app.run()