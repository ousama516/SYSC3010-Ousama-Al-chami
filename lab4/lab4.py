api_key="54CDA6FJF4RCJ92C"

from urllib.parse import urlencode
import http.client as httplib


#this sets the up teh url for thing speak
params = urlencode({'field1':"ousamaalchami@cmail.carleton.ca",'field2':"L2-M-4",'field3':"b", 'key': api_key})
headers = {"Content-typZZe": "application/x-www-form-urlencoded", "Accept": "text/plain"}

conn = httplib.HTTPConnection("api.thingspeak.com:80")
#this will try to send to thing speak
try:

    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    conn.close()
    #IF CONNECTION FAILS SEND AN ERROR
except:
    print("connection failed")

