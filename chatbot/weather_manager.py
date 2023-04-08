import requests
import json


def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=abe6b78a10df30cecbc509488f1c3957"

    response = requests.request("GET", url)
    weather_data = json.loads(response.text)

    return weather_data


def home_weather_response(city):

    weather_response_dict={}
    weather_data = get_weather_data(city)
    print(weather_data)
    weather_list = weather_data.get("weather", [])

    if len(weather_list) > 0:
        weather = weather_list[0]
        weather_main = weather.get("main", None).lower()

        if weather_main == "clouds":
            weather_main = "cloudy"

        weather_response_dict['sky'] = weather_main

    weather_list_main = weather_data.get("main", {})

    if len(weather_list_main) > 0:
        weather_degrees_fahr = weather_list_main.get("temp", None)
        weather_degrees_celsius = int(weather_degrees_fahr) - 273
        weather_degrees_feels_like = int(weather_list_main.get("feels_like", None)) - 273
        weather_degrees_min = int(weather_list_main.get("temp_min", None)) - 273
        weather_degrees_max = int(weather_list_main.get("temp_max", None)) - 273
        weather_humidity = weather_list_main.get("humidity", None)


        weather_response_dict['weather_degrees_celsius'] = weather_degrees_celsius
        weather_response_dict['weather_degrees_feels_like'] = weather_degrees_feels_like
        weather_response_dict['weather_degrees_min'] = weather_degrees_min
        weather_response_dict['weather_degrees_max'] = weather_degrees_max
        weather_response_dict['weather_humidity'] = weather_humidity


    return weather_response_dict

print(home_weather_response("bacau"))

def get_deedee_response(city):
    weather_data = get_weather_data(city)
    weather_list = weather_data.get("weather", [])
    if len(weather_list) > 0:
        weather = weather_list[0]
        weather_main = weather.get("main", None).lower()
        weather_description = weather.get("description", None)

        if weather_main == "clouds":
            weather_main = "cloudy"

    weather_list_main = weather_data.get("main", {})
    if len(weather_list_main) > 0:
        weather_degrees_fahr = weather_list_main.get("temp", None)
        weather_degrees_celsius = int(weather_degrees_fahr) - 273
        weather_degrees_feels_like = int(weather_list_main.get("feels_like", None)) - 273
        weather_degrees_min = int(weather_list_main.get("temp_min", None)) - 273
        weather_degrees_max = int(weather_list_main.get("temp_max", None)) - 273
        weather_humidity = weather_list_main.get("humidity", None)
        weather_list_main = weather_data.get("wind", {})

        if weather_humidity > 80:
            rain_status = "high"
        elif 40 < weather_humidity < 80:
            rain_status = "medium"
        elif weather_humidity > 90:
            rain_status = "extremely high"
        else:
            rain_status = "low"

    coordinates = weather_data.get("coord", {})
    # long = int(coordinates.get("lon", None))
    # lat = int(coordinates.get("lat", None))  # Bacau lon 26.9 maps_stanga lat 464667 maps_dreapta

    snow_rain_status = ""
    if weather_degrees_celsius < 0:
        snow_rain_status = "snow"
    else:
        snow_rain_status = "rain"

    if weather_degrees_feels_like == weather_degrees_celsius:
        conjunction = "and"
    else:
        conjunction = "but"

    city = city[0].upper() + city[1:len(city)]
    weather_chatbot_response = f"In {city} the sky is {weather_main}, {weather_description}\nThere are  {weather_degrees_fahr}" \
                               f" Fahrenheit degrees \nor {weather_degrees_celsius} Celsius degrees {conjunction} it feels \nlike " \
                               f"{weather_degrees_feels_like}.The maximum temperature is {weather_degrees_max}\nand the minimum temperature is" \
                               f" {weather_degrees_min}, the\nhumidity is {weather_humidity}% with {rain_status} chances to {snow_rain_status}"

    return weather_chatbot_response


def func(city):
    return get_deedee_response(city)



