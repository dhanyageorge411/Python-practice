#API (application programming interface): to access data from some other server and to intergrate to my program. Allows you to connect to code of others .

#  installed requests
#programe to get the data from apple itunes about a particular song 

import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

#URL from the documantation of apples API of itunes 

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+sys.argv[1])

#the file is in JSON format 
#to print the JSON file inmore readable format 
#print(json.dumps(response.json(),indent = 2))

#to print the tack name alone form the JSON file 

json_result = response.json()
for result in json_result["results"]:
    print(result["trackName"])



