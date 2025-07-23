# TAKE CITY OF THE USER AND THEN PRINT ITS WEATHER REPORT

import requests                                         # Import entire module

city = input("\nEnter your city: ")                     # Takes user input for the name of a city

url = f"https://wttr.in/{city}?format=3"                # Prepares the URL to get weather data.    

# 1). wttr.in is a website that shows weather in text form.
# 2). f"...{city}..." is an f-string, meaning Python will insert the value of city directly into the URL.
# 3). ?format=3 gives a short, 1-line weather summary.

response = requests.get(url)                            # Sends a GET request to the wttr.in website with your city in the URL.

print("Weather report:", response.text)                 # response.text gives the actual text content received from the website.
