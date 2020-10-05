api_key="YRETU9AN60ELIK1R"
import random
roomtemp=25
r=random.Random()
from urllib.parse import urlencode
import http.client as httplib
while(True):
    #THIS WILL CHOOSE A RANDON TEMPERATURE CLOSE TO ROMM TEMP WHICH IS AROUND 25
    temperature=roomtemp+r.randint(0,100)/100
    #this sets the up teh url for thing speak
    params = urlencode({'field1': temperature, 'key': api_key})
    headers = {"Content-typZZe": "application/x-www-form-urlencoded", "Accept": "text/plain"}

    conn = httplib.HTTPConnection("api.thingspeak.com:80")
#this will try to send the roomtemp to thing speak
    try:
        print("temperature is "+str(temperature))
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        conn.close()
        #IF CONNECTION FAILS SEND AN ERROR
    except:
        print("connection failed")
        break
