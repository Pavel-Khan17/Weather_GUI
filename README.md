# Weather_GUI

A simple PyQt5 application to fetch and display weather information based on user-provided location using the OpenWeatherMap API.

## Features

- User-friendly GUI to input location and display weather information.
- Utilizes the OpenWeatherMap API to fetch real-time weather data.
- Displays weather information such as temperature, humidity, wind speed, and weather description in a human-readable format.

## Installation

1. Clone the repository:

 ```bash
    git clone https://github.com/Pavel-Khan17/Weather_GUI.git
 ```
2. Install the required dependencies:
 ```bash
    pip install PyQt5 requests
 ```

## Usage
- Replace 'YOUR_API_KEY' in the WeatherApp class with your actual OpenWeatherMap API key.
- Run the weather_app.py script:
   ```bash
      python weather_app.py
   ```

- Enter the desired location in the input field.
- Click the "Submit" button to fetch weather information.
- A loading popup will appear while the data is being fetched.
- Once the data is retrieved, a message box will display the weather information.


