#!/usr/bin/python3

import string
import random
import sys

characters = list(string.ascii_letters + string.digits)

def generate_random_password():


	length = int(sys.argv[1])
	if len(sys.argv)<1:
		length = 8

#Tämän argumentin toiminnon kanssa minun täytyy vielä harjoitella,
# sillä se ei toimi ihan täydellisesti...

	random.shuffle(characters)
	
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	random.shuffle(password)

	print("".join(password))


generate_random_password()
