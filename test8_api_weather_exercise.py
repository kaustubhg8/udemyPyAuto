
#City,Time,Temperature,Condition

import requests

City = 'Pune'
r = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={City}&appid=3b860a33d16f5d71d87fdcc8aac4a07e&units=metric")

content = r.json()
for dict1 in content['list']:
    with open('weather_data.txt', 'a') as file:
        file.write("\n" + f"{City}" +','+ dict1['dt_txt'] +','+ str(dict1['main']['temp']) +','+ dict1['weather'][0]['description'])





print(content['list'])