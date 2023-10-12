#!/usr/bin/python

from flask import Flask
import os
import argparse
import requests
import json

app = Flask(__name__)


@app.route('/')
def main():
    # Enter your API key here
    api_key = "03c73a62f90e9a82746f188332b5c8eb"
    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # Give city name
    #city_name = input("Enter city name : ")  
    city_name = args.city_name
    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    # json method of response object 
    # convert json format data into
    # python format data
    x = response.json()
    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
         # store the value of "main"
         # key in variable y
         y = x["main"]
         # store the value corresponding
         # to the "temp" key of y
         current_temperature = y["temp"]
         #Converts from kelvin to celcius
         current_temperature=current_temperature - 273
         # store the value of "weather"
         # key in variable z
         z = x["weather"]
         # store the value corresponding 
         # to the "description" key at 
         # the 0th index of z
         weather_description = z[0]["description"]
         # print following values
         return """
         <meta http-equiv="refresh" content={} />
         Temperature (in celcius)<br><br>: {}.""".format(args.refresh,current_temperature)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("server", help="specify address and port")
    parser.add_argument("city_name", help="specify city name for openweatherapi")
    args = parser.parse_args()
    app.config.update (
       SERVER_NAME=args.server)
    app.run()
