# -*- coding: utf-8-*-
# Developped by Robin Lehn & Sebastien Glass
# Project Voice Recognition - Advanced Operating System

# Functionalities : tells the current date
# How to call it with jasper : "Jasper" - "What is the current date?"

import time
import re

WORDS = ["Date"]


def handle(text, mic, profile):
	local_time = time.localtime()

	t = time.strftime('%A the %d of %B %Y ',local_time)

	mic.say("Today, we are " + t)


def isValid(text):
	return bool(re.search(r'\b(date|which day)\b', text, re.IGNORECASE))
