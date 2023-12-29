import requests

url = "https://api.languagetoolplus.com/v2/check"

data = {
    'text': "This is a nice day",
    'language': 'auto'
}


responce = requests.post(url, data=data)

print(responce.text)