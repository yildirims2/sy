import json
import requests

base = 'https://breakingbadapi.com/api/'

resp = requests.get(base+'characters')
data = resp.json()
resp2 = requests.get(base+'deaths')
data2 = resp2.json()
a =[]
def find_occupation(c):
  global data,data2,a
  for death in data2:
    
    if death['season'] == (c):
     
      x =(death['death'])
      
      a = [x]
      
      for character in data:
        if character['name'] in a:
          print (character['name'],('--->'),character['occupation'])

find_occupation(5)