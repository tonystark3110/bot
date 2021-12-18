import speech_recognition as sr
from selenium import webdriver
import pyttsx3 as p
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests, json

class weather():
 
 

 api_key = "dcc11c58d0c15bdbb7479dadebeebb83"
 

 base_url = "http://api.openweathermap.org/data/2.5/weather?"
 

 city_name = input("Enter city name : ")
 

 complete_url = base_url + "appid=" + api_key + "&q=" + city_name
 

 response = requests.get(complete_url)
 

 x = response.json()
 

 if x["cod"] != "404":
 
    
    y = x["main"]
 
    
    current_temperature = y["temp"]
 
    
    current_pressure = y["pressure"]
 
    
    current_humidity = y["humidity"]
 
    
    z = x["weather"]
 
    
    weather_description = z[0]["description"]
    
    a=273.15
    b=25.000000000000000

    info = (" Temperature  = " +
                    str(current_temperature  - a ) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidity) +
          "\n description = " +
                    str(weather_description)   )
 
    
    print(" Temperature  = " +
                    str(current_temperature  - a ) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidity) +
          "\n description = " +
                    str(weather_description)   )

    readable_text=info
    engine = p.init()
    engine.say(readable_text)
    engine.runAndWait()               

        

 
 else:
     print(" City Not Found ")


     
       

bot = weather()








