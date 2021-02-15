import requests
import json
response = requests.get('https://breakingbadapi.com/api/quotes')
data = response.json()
a= {}
x =[]


def quotes_dict():
  global data,x
  for quote in data:
    x.append(quote["author"])


  for i in x:
   a[i] = x.count(i)
  return a
  
df = quotes_dict()
for key in df:
 print(key,df[key])