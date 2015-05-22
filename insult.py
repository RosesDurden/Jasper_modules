# Developped by Robin Lehn & Sebastien Glass
# Project Voice Recognition - Advanced Operating System

# Functionalities : respond to the user who insulted him
# How to call it with jasper : "Jasper" - "You idiot"
import re

WORDS = ["IDIOT"]

PRIORITY = 4 

def handle(text, mic, profile):
    mic.say("Go fuck your self !")


def isValid(text):
    return bool(re.search(r'\byou idiot\b', text, re.IGNORECASE))
