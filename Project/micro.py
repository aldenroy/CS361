import time
import requests

while True:
    time.sleep(1)
    with open("weather-service.txt", "r") as file:
        city = file.readline().strip()
    
    if(city[:3] == "run"):
        api_key = 'd9eed6b80a1c4271974224250233110'
        location = str(city[3:])

        # Define the API endpoint and parameters
        endpoint = 'http://api.weatherapi.com/v1/current.json'
        params = {
            'key': api_key,
            'q': location,
        }

        # Make the API request
        response = requests.get(endpoint, params=params)
        

        if response.status_code == 200:
            # Request was successful
            data = response.json()
            current_weather = data['current']
            temperature = current_weather['temp_c']
            condition = current_weather['condition']['text']

        else:
            # Request failed
            print(f"Failed to retrieve weather data. Status code: {response.status_code}")
        
        with open("weather-service.txt", "w") as file:
            file.truncate(0) #erase run
            file.write("Weather in " + location + ": " + str(temperature) + "°C, " + condition)
        file.close()