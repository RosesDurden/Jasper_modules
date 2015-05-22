# -*- coding: utf-8-*-
# Developped by Robin Lehn & Sebastien Glass
# Project Voice Recognition - Advanced Operating System

# Functionalities : tells the user which movies are new at the cinema
# How to call it with jasper : "Jasper" - "What's the last movies at the cinema?"
import os
import re
import subprocess
import datetime
import urllib
import requests
from bs4 import BeautifulSoup

WORDS = ["Last", "Movies"]
 
# retourne liste
def customRange(start, end, step):
    while start <= end:
        yield start
        start += step

#retourne transforme string en float
def floatFromStringValue(str):
	str =str.replace(',','.')
	return float(str)


# affiche les films 
def display_movies(movies, real, notes):
	note =""
	print("===================================")
	print("The last movies are :")
	for i in range(0,5):
		for j in range(0,notes[i]):
			note += "*"
		print( movies[i].find('a').string.strip() + " - Realisateur : " + real[i].strip() + " - Note : " + note)
		note =""
	print("==================================")
		
#recherche les 5 derniers films
def search_movies(content):
	data = content.find_all("h2","tt_18 d_inline j_entities",limit=5)
	return data

#recherche les realisateurs des 5 derniers films
def search_realisateurs(content):	
	data1 = content.find_all("table","data_box_table margin_10b",limit=5)
	data2 = []
	for row in data1:
		data2.append(row.find('tr').find_next('tr').find('span').find_next('span').string)
	return data2
	
#recherche les notes des 5 derniers films
def search_note(content):
	data = content.find_all("span","note",limit=10)
	data2 = []
	for i in customRange(0,9,2):
		data2.append(int((floatFromStringValue(data[i].find('span').string) + floatFromStringValue(data[i].find('span').string))/2 ))
	return data2

# annonce les derniers films trouvés
def tells_movies(movies, mic):
	mic.say("The last movies are ")
	for i in range(0,5):
		mic.say(movies[i].find('a').string.strip())

# execute lorsque jasper reconnait la commande
def handle(text, mic, profile):	
	r = requests.get('http://www.allocine.fr/film/sorties-semaine')
	soup = BeautifulSoup(r.text)
	movies = search_movies(soup)
	real = search_realisateurs(soup)
	notes = search_note(soup)
	display_movies(movies, real, notes)
	tells_movies(movies, mic)

# verifie si la commande correspond
def isValid(text):
    return bool(re.search(r'\blast movies\b', text, re.IGNORECASE))
