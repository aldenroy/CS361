import requests
import time
print("Welcome to the CS361 weather app")
print("You can enter 4 to exit, b to go back one, h to come back to the home page.")
print("Enter 1 to continue")
print("Enter 2 to enter your city")
print("Enter 3 to convert temperature")
user_input = input("Enter your choice: ")

while user_input != "4":
    if user_input == "h":
        print("Welcome to the CS361 weather app")
        print("You can enter 4 to exit, b to go back one, h to come back to the home page.")
        print("Enter 1 to continue")
        print("Enter 2 to enter your city")
        print("Enter 3 to convert temperature")
        user_input = input("Enter your choice: ")
        
    if user_input == "1":
        country = input("Enter your country: ")
        #follow order in your doc
        if country == "h":
            user_input = "h"
        elif country == "b":
            user_input = "h"
            #send home or back by input
        else:
            user_input = "2"

    elif user_input == "2":
        city = input("Enter your city: ")
        if city == "h":
            user_input = "h"
        elif city == "b":
            user_input = "1"
            #send home or back by input
        else:
            user_input = "3"
            
            with open("weather-service.txt", "w") as weather:
                weather.write("run" + city)
            time.sleep(5)
            
            with open("weather-service.txt", "r") as weather:
                weather_content = weather.read()
                
            # with open("image-service.txt", "w") as image:
            #     image.truncate(0)
            #     image.write(str(prng_content))
            # time.sleep(5)
            
            # with open("image-service.txt", "r") as file:
            #     content = file.read()
            
            print(weather_content)
            weather.close()
            # image.close()
            # Replace 'YOUR_API_KEY' with your actual WeatherAPI.com API key



    elif user_input == "3":
        choice = input("Enter 1 to convert from C to F 2 to convert F to C: ")
        if choice == "h":
            user_input = "h"
        elif choice == "b":
            user_input = "2"
            #send home or back by input
        elif choice == "1":
            temp = input("Enter your temp in Celsius: ")
            if temp[0].isdigit():
                temp = int(temp)
                converted = (temp * 1.8) + 32
                print(str(temp) +  " degrees C is " + str(converted) + " degrees F")
            else:
                print("Please enter a valid temperature.")


        elif choice == "2":
            temp = input("Enter your temp in Fahrenheit: ")
            if temp[0].isdigit():
                temp = int(temp)
                converted = (temp - 32) * (5/9)
                print(str(temp) +  " degrees F is " + str(converted) + " degrees C")
            else:
                print("Please enter a valid temperature.")


    elif user_input == "4":
        pass
    
    else:
        print("Invalid choice")
        print("You can enter 4 to exit, b to go back one, h to come back to the home page.")
        print("Enter 1 to continue")
        print("Enter 2 to enter your city")
        print("Enter 3 to convert temperature")
        user_input = input("Enter your choice: ")
        

# Specify the location you want to get weather data for (Portland, Oregon in this case)

