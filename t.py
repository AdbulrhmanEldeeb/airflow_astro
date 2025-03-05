import requests
LAT, LON = '51.5074', '-0.1278'
url = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current_weather=true"
response = requests.get(url)
print(response.json())