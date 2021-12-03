import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Senior Citizen':0, 'Tenure':9, 'Monthly Charges':60})

print(r.json())