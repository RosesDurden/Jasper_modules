# Developped by Robin Lehn & Sebastien Glass
# Project Voice Recognition - Advanced Operating System

# Functionalities : scream for you
# How to call it with jasper : "Jasper" - "Scream for me"
import re


WORDS = ["SCREAM"]


def handle(text, mic, profile):
    base_path = '/home/pi/jasper/client/modules/Songs/'
    songToPlay = base_path + 'Wont_Get_Fooled_Again.wav'
    mic.speaker.play(songToPlay)
    
	


def isValid(text):
    return bool(re.search(r'\b(scream (for me|loud)|Do you feel good)\b', text, re.IGNORECASE))
