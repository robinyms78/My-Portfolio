import json
import csv
from collections import defaultdict
import requests
from pprint import pprint
from information.place import Place

columns = defaultdict(list)

API_Key = "564400a0b8185ea1aef480134ae1934f"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


class Weather:
    def __init__(self, timestamp, weather, wind, humidity, temperature, place):
        self.timestamp = timestamp
        self.weather = weather
        self.wind = wind
        self.humidity = humidity
        self.temperature = temperature
        self.place = place

    # Get weather data from zip code
    def get_weather_data(self):
        place = Place("NA")
        self.zipcode = place.get_zip_code()
        final_url = base_url + "appid=" + API_Key + "&q=" + self.zipcode
        self.weather_data = requests.get(final_url).json()
        #print("\nWeather Data By Zip Code: ", self.weather_data)
        pprint(self.weather_data)
        self.update()
        return self.weather_data

    def update(self):
        self.timestamp = self.process_timestamp()
        self.weather = self.process_weather()
        self.wind = self.process_wind()
        self.humidity = self.process_humidity()
        self.temperature = self.process_temperature()
        self.place = self.get_place()

    # Process timestamp
    def process_timestamp(self):
        self.timestamp = self.weather_data["dt"]
        return self.timestamp

    # Process main weather information
    def process_weather(self):
        self.weather = self.weather_data["weather"][0]["description"]
        self.weather = list(self.weather.split(" "))
        for element in self.weather:
            if "rain" in element:
                self.weather = "rain"
            elif "cloud" in element:
                self.weather = "clear"
            elif "snow" in element:
                self.weather = "snow"
        return self.weather

    # Process wind information
    def process_wind(self):
        self.wind = self.weather_data["wind"]["speed"]
        if int(self.wind) < 11:
            self.wind = "light wind"
        elif 12 < int(self.wind) < 28:
            self.wind = "gentle moderate wind"
        elif 29 < int(self.wind) < 38:
            self.wind = "fresh wind"
        elif 39 < int(self.wind) < 61:
            self.wind = "string wind"
        elif 62 < int(self.wind) < 88:
            self.wind = "gale"
        elif 89 < int(self.wind) < 117:
            self.wind = "whole gale"
        else:
            self.wind = "hurricane"
        return self.wind

    # Process humidity information
    def process_humidity(self):
        self.humidity = self.weather_data["main"]["humidity"]
        if int(self.humidity) < 30:
            self.humidity = "dry"
        elif 30 < int(self.humidity) < 70:
            self.humidity = "humid"
        else:
            self.humidity = "extremely humid"
        return self.humidity

    # Process temperature information
    def process_temperature(self):
        self.temperature = self.weather_data["main"]["temp"]
        # Convert temperature from Kelvin to degree celsius
        self.temperature = int(self.temperature) - 273
        if int(self.temperature) <= 10:
            self.temperature = "very cold"
        elif 10 < int(self.temperature) <= 20:
            self.temperature = "cold"
        elif 20 < int(self.temperature) <= 27:
            self.temperature = "good"
        elif 27 < int(self.temperature) <= 35:
            self.temperature = "hot"
        else:
            self.temperature = "very hot"
        return self.temperature

    def get_place(self):
        self.place = self.weather_data["name"]
        return self.place

    # Parse weather information to JSON
    def get_json(self):
        weather_information = {"timestamp": self.timestamp,
                               "place": self.get_place(),
                               "weather": self.weather,
                               "wind": self.wind,
                               "humidity": self.humidity,
                               "temperature": self.temperature}
        weather_information = json.dumps(weather_information)
        return weather_information

    # Parse dummy weather information to JSON from CSV file
    def get_json_csv(self):
        with open("information/weather.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                for(k, v) in row.items():
                    columns[k].append(v)
        self.timestamp = columns["timestamp"][0]
        self.place = columns["place"][0]
        self.weather = columns["weather"][0]
        self.wind = columns["wind"][0]
        self.humidity = columns["humidity"][0]
        self.temperature = columns["temperature"][0]
        weather_information = {"timestamp": self.timestamp,
                               "place": self.place,
                               "weather": self.weather,
                               "wind": self.wind,
                               "humidity": self.humidity,
                               "temperature": self.temperature}
        weather_information = json.dumps(weather_information)
        #print(weather_information)
        return weather_information


# Create weather object
weather_supplicant = Weather("0", "clear", "wind", "humid", "hot", "Tokyo")

