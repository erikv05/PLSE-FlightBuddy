from flask import Flask, request
import hashlib
app = Flask(__name__)

@app.route('/preditct', methods=['POST'])
def predict():
    if 'flight_number' not in request.json:
        return 400, {'err': 'No flight number to predict!'}
    else:
        200, {"prediction" : hashlib.sha256(str(request.json.flight_number).encode('utf-8')).hexdigest() % 5}
