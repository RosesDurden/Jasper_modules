# Developped by Robin Lehn & Sebastien Glass
# Project Voice Recognition - Advanced Operating System

# Functionalities : powers on a LED
# How to call it with jasper : "Jasper" - "Turn the lights on?"

import re
import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'


WORDS = ["TURN", "LIGHT", "ON"]

def handle(text, mic, profile):
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
    GPIO.output(7,True) ## Turn on GPIO pin 7

def isValid(text):
    return bool(re.search(r'\blight on\b', text, re.IGNORECASE))