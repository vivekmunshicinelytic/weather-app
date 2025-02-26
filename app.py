from flask import Flask, render_template, request
import requests
import var
import os

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
    city = "London" # Default city
    api_key = os.getenv("WEATHER_API_KEY", "62c5ae"
    if request.method == 'POST':
        city = request.form['city']
        api_key = var.key
        weather_data = get_weather(api_key, city)
        transcode_data = { }
    
    return render_template('index.html', transcode_data=None)

if __name__ == "__main__":
    #app.run(debug=True,port=8080)
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)

