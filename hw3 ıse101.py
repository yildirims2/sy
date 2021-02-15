import requests
import json

def find_titles(character_count):
    
 
    url="https://www.breakingbadapi.com/api/episodes"
  

  
    response = requests.get(url)
  

    response_dict = json.loads(response.text)
  

    for res in response_dict:
  
         no_of_characters=len(res['characters'])
  
         if no_of_characters==character_count:
             print("season number:",res['season'],end="\t")
             print("episode number:",res['episode_id'],end="\t")
             print("title:",res['title'],end="\n")
  
  
  
find_titles(12)