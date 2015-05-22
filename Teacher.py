# Developped by Robin Lehn & Sebastien Glass
# Project Voice Recognition - Advanced Operating System

# Functionalities : tells the user who is the best teacher
# How to call it with jasper : "Jasper" - "Who is the best teacher?"
import re

WORDS = ["BEST", "TEACHER"]

PRIORITY = 4 

def handle(text, mic, profile):
    mic.say("The best teatcher is Mister Naegel")


def isValid(text):
    return bool(re.search(r'\bbest teacher\b', text, re.IGNORECASE))
