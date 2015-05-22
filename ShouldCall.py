# Developped by Robin Lehn & Sebastien Glass
# Project Voice Recognition - Advanced Operating System

# Functionalities : tells me with a song who i should call
# How to call it with jasper : "Jasper" - "who should i call?"
import re
import random

WORDS = ["Call"]

PRIORITY = 2 

def randomSong():
    base_path = '/home/pi/jasper/client/modules/Songs/'
    songs = ['Better_Call_Saul.wav','ghostbusters.wav']
    song = random.choice(songs)
    return base_path + song
    

def handle(text, mic, profile):
    songToPlay = randomSong()
    mic.speaker.play(songToPlay)


def isValid(text):
    return bool(re.search(r'\bwho (should|must|can|could) (we|I|you|they|he|she) call\b', text, re.IGNORECASE))
