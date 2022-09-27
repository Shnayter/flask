from __future__ import print_function
import requests
import json
import cv2

addr = 'http://localhost:5000/datas'
test_url = addr 

content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = cv2.imread('/home/shnayter/img.jpg')

_, img_encoded = cv2.imencode('.jpg', img)

response = requests.post(test_url, data=img_encoded.tobytes(), headers=headers)

print(json.loads(response.text))
