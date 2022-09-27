from flask import Flask, request, jsonify
from flask import session
import requests
import json
import cv2 
import numpy as np

app = Flask(__name__)



@app.route('/datas', methods=['POST'])
def datas():
    r = request
    
    nparr = np.fromstring(r.data, np.uint8)
    
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    return jsonify(response)


        

if __name__ == '__main__':
    app.run(debug=True)
