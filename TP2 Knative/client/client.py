import requests
import json
import time
import random

FUNCTION_IP_ADDRESS="localhost:8888"

url = 'http://' + FUNCTION_IP_ADDRESS + '/data'

while True:
    temperature = round(random.uniform(10, 40), 2)
    humidity = round(random.uniform(20, 80), 2)
    luminosity = round(random.uniform(0, 100), 2)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    data = {
        "temperature": temperature,
        "humidity": humidity,
        "luminosity": luminosity,
        "timestamp": timestamp
    }
    
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print("Data sent to serverless function:", r.text)
    
    time.sleep(30)
