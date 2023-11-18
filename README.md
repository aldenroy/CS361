# CS361
Communication Contract: We will use teams for commmunication. For responsiveness, members should respond to messages the same day/within 24 hours of receiving the message. For meetings, we will define a regular meeting schedule that works for all team members and ensures that everyone can plan their availability and participation. For task division we can use a rotating system to basically bounce our work back and forth to each other when one person needs to work on the microservice for the other. If a conflict arises we will involve open discussions, or seek input from the instructor. 

Requesting data: Run python3 project.py then enter 2 to input a city. Put a city name such as Portland, and this will make a call to the api to get you your data.

            # Define the API endpoint and parameters
            api_key = 'd9eed6b80a1c4271974224250233110'
            location = str(city)
            endpoint = 'http://api.weatherapi.com/v1/current.json'
            params = {
                'key': api_key,
                'q': location,
            }

            # Make the API request
            response = requests.get(endpoint, params=params)
This is basically the call
To receive data just do what I said above and the requests.get() method will return you weather data.
ie Weather in Portland: 12.8°C, Partly cloudy
UML Diagram:

<img width="502" alt="image" src="https://github.com/aldenroy/CS361/assets/39741981/8128f330-11b0-4b9d-9c5b-aa9aeff9663b">
