
import requests


r = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2023-09-03&sortBy=publishedAt&apiKey=9728c6b176774bffb7180afbb4458712')

content = r.json()
arti = content['articles']
print(arti)