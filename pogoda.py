from dotenv import load_dotenv
#from pprint import pprint
import os
import requests
#import tkinter as tk
#from tkinter import Tk, Label

load_dotenv()
params = {
    "key": os.getenv("WEATHER_API_KEY"),
    "q": "auto:ip",
    "aqi": "aqi=yes",
    "lang": "lang=pl",
}
r = requests.get("http://api.weatherapi.com/v1/current.json", params)
data = r.json()

#Only for testing
#pprint(data) #- print all content of json file
#

#API VARIABLES
location = data["location"]["name"]
local_feelslike_c=data["current"]["feelslike_c"]
local_feelslike_f=data["current"]["feelslike_f"]
local_gust_kph=data["current"]["gust_kph"]
local_gust_mph=data["current"]["gust_mph"]
local_wind_kph=data["current"]["wind_kph"]
local_wind_mph=data["current"]["wind_mph"]
local_humidity = data["current"]["humidity"]
local_temperature = data["current"]["temp_c"]
temperature_in_farenheit = "%.1f" % (float(local_temperature * 1.8) + 32)
temperature_in_celvin = local_temperature + 273.15

"""
#WINDOW
window = tk.Tk()
window.title("Pogoda")
window.geometry("800x600")
naglowek = Label(window, text="Pogoda w twoim mieście", font=("Arial Bold", 50))
label1 = Label(window, text="Znajdujesz się w miejscowości: "+ str(location), font=("Arial Bold", 25))
label2 = Label(window, text="Odczuwalna temperatura: "+ str(local_feelslike_c)+ "℃", font=("Arial Bold", 25))
label3 = Label(window, text="Temperatura panująca lokalnie: "+ str(local_temperature)+ "℃", font=("Arial Bold", 25))
label4 = Label(window, text="Wilgotność na poziomie: "+ str(local_humidity)+ "%", font=("Arial Bold", 25))
label5 = Label(window, text="Prędkość Wiatru: "+ str(local_wind_kph)+ " km/h", font=("Arial Bold", 25))

naglowek.pack()
label1.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()


window.mainloop()



"""
print(f"Znajdujesz się w miejscowości: {location} \nTemperatura panująca lokalnie: {local_temperature}℃ \nWilgotność na poziomie: {local_humidity}% \nPrędkość Wiatru: {local_wind_kph}KM/H \nTemperatura w Farnehite: {temperature_in_farenheit}℉ \nTemperatura w Kelvinach: {temperature_in_celvin} K"
)
