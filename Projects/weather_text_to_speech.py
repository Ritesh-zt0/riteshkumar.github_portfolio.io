import os
import requests
import json
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

city = input("Enter the name of the city: \n")

url = f"https://api.weatherapi.com/v1/current.json?key=a94de503031344f886f153530231105&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

while 1:
    speaker.Speak(f" The current weather in {city} is {w} degrees")

# Close the terminal for the output voice to stop.



