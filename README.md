# 🌤️ Weather CLI

A simple command-line weather application built with Python.

The application takes a city name from the user, finds its geographic coordinates using the Open-Meteo Geocoding API, and then retrieves the current hourly temperature data from the Open-Meteo Weather API.

## ✨ Features

- Search weather by city name
- Convert city name to latitude and longitude
- Fetch hourly temperature data from an API
- Display the next 5 hourly temperatures
- Clean and readable terminal output
- Handles cities that cannot be found
- Handles weather API request errors
- Uses functions to separate responsibilities
- Uses HTTP status code handling
- Works with JSON API responses

## 🧠 What I Learned

While building this project, I practiced:

- Using external APIs with Python
- The `requests` library
- HTTP requests and response status codes
- `requests.get()`
- Query parameters with `params`
- `response.json()`
- `response.raise_for_status()`
- Exception handling with `try / except`
- Working with nested dictionaries and lists
- Extracting data from JSON responses
- Handling API responses with empty results
- Function design and separation of responsibilities
- Returning `None` when an operation fails
- Working with latitude and longitude
- Refactoring code into smaller functions

## 🔌 APIs Used

This project uses the Open-Meteo APIs:

- Open-Meteo Geocoding API — converts a city name into geographic coordinates
- Open-Meteo Weather API — provides hourly weather data

## 📁 Project Structure

```text
weather_cli/
│
├── main.py
└── README.md
```

## ▶️ How to Run

Make sure Python is installed on your computer.

Install the required package:

```bash
pip install requests
```

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Go into the project directory:

```bash
cd weather_cli
```

Run the application:

```bash
python main.py
```

## 💻 Example

```text
Enter city: Baku

🌤️ Weather for Baku

17:00 → 24.3°C
18:00 → 23.8°C
19:00 → 23.1°C
20:00 → 22.5°C
21:00 → 21.9°C
```

## ⚠️ Error Handling

The application handles common situations such as:

- City not found
- Empty API search results
- Weather API request errors
- Invalid API responses caused by HTTP errors

## 🛠️ Technologies

- Python 3
- Requests
- REST APIs
- JSON
- Git
- GitHub
