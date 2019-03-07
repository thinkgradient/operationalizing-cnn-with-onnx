from flask import Flask
from flask import request
import numpy as np
import cv2
import score
import json

app = Flask(__name__)

score.init()

@app.route("/")
def intro():
    return "welcome to ONNX operationalize ML models"

@app.route("/api/classify_digit", methods=['POST'])
def classify():
    input_img = np.fromstring(request.data, np.uint8)
    img = cv2.imdecode(input_img, cv2.IMREAD_GRAYSCALE)
    classify_response = "".join(map(str, score.run(img)))
    json_prediction = json.loads(classify_response)
    predicted_number = 0
    for i in range(0,9):
    	if float(json_prediction["prediction"][0][0][i]) > 0.5:
    			predicted_number = i
    			break

    return (str(predicted_number))

if __name__ == 'main':
    app.run(debug = True, host='0.0.0.0')

