from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/predict')
@cross_origin()
def predict():
    if not request.args.get('number'):
        return jsonify({'err': 'No flight number to predict!'}), 400
    else:
        try:
            hashNum: int = hash(request.args.get('number')) % 10
            print(hashNum)
            prediction: int
            match hashNum:
                case hashNum if 0 <= hashNum <= 3:
                    prediction = 0
                case hashNum if 4 <= hashNum <= 5:
                    prediction = 1
                case hashNum if 6 <= hashNum <= 7:
                    prediction = 2
                case 8:
                    prediction = 3
                case 9:
                    prediction = 4
            
            return jsonify({"prediction": prediction}), 200
        except Exception as e:
            return jsonify({'err': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8088)