import requests
#read the thingsspeaks channel
api_key= "https://api.thingspeak.com/channels/1174085/feeds.json?api_key=8C9K1N3ZQLYEV0JN&results=2"
thingspeaksdata = requests.get(api_key)
jsontext=thingspeaksdata.json()
print(jsontext)
#read the json data
field1=jsontext.get("feeds")
outputtext=[]
for text in field1:
    outputtext.append(text["field1"])
print (outputtext)


