'''
Description: Monte Carlo simulation that estimates the value of pi through repeated rounds of increasing points

Installing Python/Pygame on Mac:
1) xcode-select --install
2) ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
3) brew install python3 hg sdl sdl_image sdl_mixer sdl_ttf portmidi
4) pip3 install hg+http://bitbucket.org/pygame/pygame

To Run:
$ python3 throwpoints.py
'''

import random
import math
import pygame
from pygame.locals import *
import sys

#define constants
START_POINTS = 100
END_POINTS = 10000
MULTIPLIER = 10
WIDTH = 500
HEIGHT = 500
RADIUS = 250

#initialize counters
currentTestRound = 1
totalTestRounds = 5
totalPoints = 1
pointsInCircle = 0
pointsToThrow = START_POINTS


screen = pygame.display.set_mode((WIDTH, HEIGHT))
for event in pygame.event.get():
	while pointsToThrow <= END_POINTS: #pointsToThrow is multiplied at the end
		print ("\nThrowing %d points" % pointsToThrow)
		while currentTestRound <= totalTestRounds:
			circle = pygame.draw.circle(screen, (0,0,255), (RADIUS, RADIUS), 250, 1)
			while totalPoints < pointsToThrow:
				x = int(500*random.random())
				y = int(500*random.random())
				distance = math.hypot(x-(WIDTH/2.0), y-(HEIGHT/2.0))
				if distance < RADIUS:
					point = pygame.draw.circle(screen, (0,0,255), (x, y), 0, 0) #sets a blue point inside circle
					pointsInCircle += 1
					totalPoints += 1
				elif distance > RADIUS:
					point = pygame.draw.circle(screen, (255,0,0), (x, y), 0, 0)	#sets a red point outside circle
					totalPoints +=1
				pygame.display.update()

			sys.stdout.flush()
			piApprox = 4.0 * float(pointsInCircle)/float(totalPoints)
			print ("Trial #%d: %f" % (currentTestRound, piApprox))
			pygame.time.wait(4000) #pause screen for 2 seconds

			#reset counters
			totalPoints = 0
			pointsInCircle = 0
			currentTestRound += 1
			screen.fill((0, 0, 0))
		pointsToThrow *= MULTIPLIER # multiplies pointsThrown for new set of test rounds
		currentTestRound = 1 # reset currentTestRound
		
pygame.display.update()
