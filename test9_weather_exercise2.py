import requests
#City,Time,Temperature,Condition

def get_weather(city, units='metric', api_key = '3b860a33d16f5d71d87fdcc8aac4a07e'):
    r = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}")
    content = r.json()
    # return content

    with open('weather_data.txt', 'a') as file:
        for dicty in content['list']:
            file.write(f"\n{city}, {dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}")


get_weather("Pune")