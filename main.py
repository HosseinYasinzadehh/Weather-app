import requests

city = input("Enter city: ")


def get_coordinates(city):
    params = {
        "name": city
    }

    url = "https://geocoding-api.open-meteo.com/v1/search"

    response = requests.get(url, params=params)

    if response.status_code == 200:
        final = response.json()

        if final["results"]:
            lat = final["results"][0]["latitude"]
            lng = final["results"][0]["longitude"]

            return lat, lng

        else:
            return None


def get_weather(latitude, longitude):
    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m"
    }

    weather_url = "https://api.open-meteo.com/v1/forecast"

    response_weather = requests.get(weather_url, params=weather_params)

    try:
        response_weather.raise_for_status()
        data = response_weather.json()
        return data

    except requests.exceptions.RequestException:
        return None


coordinates = get_coordinates(city)

if coordinates:
    lat, lng = coordinates

    data = get_weather(lat, lng)

    if data:
        print(f"\n🌤️ Weather for {city}\n")

        for item in range(5):
            time = data["hourly"]["time"][item].split("T")[1]
            temperature = data["hourly"]["temperature_2m"][item]

            print(f"{time} → {temperature}°C")

    else:
        print("data error")

else:
    print("City not found")