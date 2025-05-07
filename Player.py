import pygame
import pygwidgets
from Constants import *

class Player():
    def __init__(self, window):
        self.window = window
        self.x = 100
        self.y = 100
        self.image = pygwidgets.Image(self.window, (self.x, self.y), 'images/player.png')
        self.speed = 5
        self.hasShield = False
        self.slowMotionActive = False
        self.slowMotionTimer = 0
        self.shieldTimer = 0

    def update(self, mouseX, mouseY):
        self.x = mouseX - self.image.getRect().width // 2
        self.y = mouseY - self.image.getRect().height // 2
        self.image.setLoc((self.x, self.y))

        if self.slowMotionActive:
            self.slowMotionTimer -= 1
            if self.slowMotionTimer <= 0:
                self.deactivateSlowMotion()

        if self.hasShield:
            self.shieldTimer -= 1
            if self.shieldTimer <= 0:
                self.deactivateShield()

        return self.image.getRect()

    def applyOrbEffect(self, orb_type):
        if orb_type == ORB_TYPE_SPEED:
            self.activateSpeed()
        elif orb_type == ORB_TYPE_SHIELD:
            self.activateShield()
        elif orb_type == ORB_TYPE_SLOW:
            self.activateSlowMotion()

    def activateSpeed(self):
        self.speed += 2

    def activateShield(self):
        self.hasShield = True
        self.shieldTimer = SHIELD_DURATION

    def deactivateShield(self):
        self.hasShield = False

    def activateSlowMotion(self):
        self.slowMotionActive = True
        self.slowMotionTimer = SLOW_MOTION_DURATION

    def deactivateSlowMotion(self):
        self.slowMotionActive = False

    def isShieldActive(self):
        return self.hasShield

    def isSlowMotionActive(self):
        return self.slowMotionActive

    def draw(self):
        self.image.draw()
        if self.hasShield:
            centerX = self.x + self.image.getRect().width // 2
            centerY = self.y + self.image.getRect().height // 2
            radius = max(self.image.getRect().width, self.image.getRect().height) // 2 + 10
            pygame.draw.circle(self.window, (0, 100, 255), (centerX, centerY), radius, 3)  # Blue ring
