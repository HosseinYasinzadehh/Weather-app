import requests

city = input("Enter city: ")

def get_coordinates(city):
    params = {
        "name": city
    }
    url = "https://geocoding-api.open-meteo.com/v1/search"

    response = requests.get(url,params=params)

    if response.status_code == 200:
        final = response.json()

        if final['results']:
            lat = final['results'][0]['latitude']
            lng = final['results'][0]['longitude']
            return lat, lng

        else:
            return None
    


coordinates = get_coordinates(city)
if coordinates:
    lat, lng = coordinates
    
    weather_params = {
        "latitude": lat,
        "longitude": lng,
        "hourly": "temperature_2m"
        
    }

    weather_url = "https://api.open-meteo.com/v1/forecast"

    response_weather = requests.get(weather_url,params=weather_params)

    try:
        response_weather.raise_for_status()
        data = response_weather.json()
        print(f'{data["hourly"]["time"][0]} : {data["hourly"]["temperature_2m"][0]}')
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
else:
    print("City not found")


