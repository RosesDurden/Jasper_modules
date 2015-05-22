# Developped by Robin Lehn & Sebastien Glass
# Project Voice Recognition - Advanced Operating System

# Functionalities : tells the distance and duration between two given adress
# How to call it with jasper : "Jasper" - "How far is ... from ... ?"
import re
import urllib
import json



WORDS = ["Destination", "origin", 'from', "to"]

# gets the origin location from the string
def getOriginLocation(text):
	origin = ""
	# try to match to the following pattern to extract the origin
	origin_search = re.search(r'\bHow (long|far) .*(is .* from (.*)|from (.*) is .*|to .* from (.*)|from (.*) to .*)\b',text, re.IGNORECASE)
	if bool(origin_search): 
		
		for i in range(3, 6):
			tmp = origin_search.group(i)
			if tmp != None:
				origin = tmp
		
	return origin

# gets the destination location from the string
def getDestinationLocation(text):
	destination = ""
	# try to match to the following pattern to extract the destination
	destination_search = re.search(r'\bHow (long|far) .*(is (.*) from .*|from .* is (.*)|to (.*) from .*|from .* to (.*))\b',text, re.IGNORECASE)
	if bool(destination_search): 
		
		for i in range(3, 6):
			tmp = destination_search.group(i)
			if tmp != None:
				destination = tmp
		
	return destination
	
# display the distance information 
def display(distance, origine, destination):
	print("===================================")
	print("The distance between "+origine+" and "+destination +" : " )
	print(distance)
	print("==================================")
		
		
# returns the location of "home"
def getsHome(profile):
	if 'location' in profile:
		home = get_forecast_by_name(str(profile['location']))
	else:
		home = ""
		
	return home

def handle(text, mic, profile):
	destination = getDestinationLocation(text)
	origin = getOriginLocation(text)
	
	# if the origin is home
	if origin == "home" :
		origin = getsHome(profile)
	
	# if the destination is home
	if destination == "home" :
		destination = getsHome(profile)
	
	url = "https://maps.googleapis.com/maps/api/directions/json?language=en&origin="+origin+"&destination="+destination
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	
	
	if data["status"] == "OK" : # if no error
		res = "The ride is " +data["routes"][0]["legs"][0]["distance"]["text"] + " long and will last " + data["routes"][0]["legs"][0]["duration"]["text"] + " by car"
		resDisplay = data["routes"][0]["legs"][0]["distance"]["text"] + " - " + data["routes"][0]["legs"][0]["duration"]["text"]
	else :
		res = data["status"]
		resDisplay = data["status"]
	
	display(resDisplay,  origin, destination)
	mic.say(res);

def isValid(text):
    return bool(re.search(r'\bHow (long|far) .*(is .* from .*|from .* is .*|to .* from .*|from.* to .*)\b', text, re.IGNORECASE))
