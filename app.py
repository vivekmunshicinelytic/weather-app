from flask import Flask, render_template, request
import requests
import var
import os
import json

app = Flask(__name__)

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            return None

    except Exception as e:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    data = request.get_json(silent=True) or {}
    
    city = request.form.get("city", "London")
    api_key = os.getenv("WEATHER_API_KEY", "62c5ae06c3c40af76390a238bb76c7dd")
    
    # if request.method == 'POST':
        # city = request.form['city']
        # api_key = var.key
    
    transcode_data = {
        "SOURCE_FILE_NAME": data.get("SOURCE_FILE_NAME", os.getenv("SOURCE_FILE_NAME", "Not Set")),
        "SourceBucketName": data.get("SourceBucketName", os.getenv("SourceBucketName", "Not Set")),
        "DestBucketName": data.get("DestBucketName", os.getenv("DestBucketName", "Not Set"))
    }
    weather_data = get_weather(api_key, city)
    return render_template('index.html', weather_data=weather_data, transcode_data=transcode_data)

if __name__ == "__main__":
    #app.run(debug=True,port=8080)
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)

