import pygame
import pygwidgets
import random
from Constants import *

class Baddie():
    MIN_SIZE = 10
    MAX_SIZE = 40
    MIN_SPEED = 1
    MAX_SPEED = 8
    BADDIE_IMAGE = pygame.image.load('images/baddie.png')

    def __init__(self, window, speed=None):
        self.window = window
        size = random.randrange(Baddie.MIN_SIZE, Baddie.MAX_SIZE + 1)
        self.x = random.randrange(0, WINDOW_WIDTH - size)
        self.y = 0 - size
        self.image = pygwidgets.Image(self.window, (self.x, self.y), Baddie.BADDIE_IMAGE)
        percent = (size * 100) / Baddie.MAX_SIZE
        self.image.scale(percent, False)
        self.baseSpeed = random.randrange(Baddie.MIN_SPEED, Baddie.MAX_SPEED + 1) if speed is None else speed

    def update(self, slowMotionActive=False):
        effectiveSpeed = self.baseSpeed // 2 if slowMotionActive else self.baseSpeed
        self.y += effectiveSpeed
        self.image.setLoc((self.x, self.y))
        return self.y > GAME_HEIGHT

    def draw(self):
        self.image.draw()

    def collide(self, playerRect):
        return self.image.overlaps(playerRect)

class BaddieMgr():
    ADD_NEW_BADDIE_RATE = 8

    def __init__(self, window):
        self.window = window
        self.reset()

    def reset(self):
        self.baddiesList = []
        self.nFramesTilNextBaddie = BaddieMgr.ADD_NEW_BADDIE_RATE
        self.slowMotionActive = False  # Track state

    def setSlowMotion(self, slowMotionOn):
        self.slowMotionActive = slowMotionOn

    def update(self):
        nBaddiesRemoved = 0
        for oBaddie in self.baddiesList[:]:
            if oBaddie.update(self.slowMotionActive):
                self.baddiesList.remove(oBaddie)
                nBaddiesRemoved += 1

        self.nFramesTilNextBaddie -= 1
        if self.nFramesTilNextBaddie <= 0:
            self.baddiesList.append(Baddie(self.window))
            self.nFramesTilNextBaddie = BaddieMgr.ADD_NEW_BADDIE_RATE

        return nBaddiesRemoved

    def draw(self):
        for oBaddie in self.baddiesList:
            oBaddie.draw()

    def hasPlayerHitBaddie(self, playerRect, shieldActive):
        for oBaddie in self.baddiesList:
            if oBaddie.collide(playerRect):
                if shieldActive:
                    self.baddiesList.remove(oBaddie)
                    return False  # Player is protected
                return True
        return False
