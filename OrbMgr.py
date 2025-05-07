import random
from Orb import Orb
from Constants import *

class OrbMgr():
    def __init__(self, window):
        self.window = window
        self.reset()

    def reset(self):
        self.orbsList = []
        self.nFramesTilNextOrb = random.randint(ORB_RATE_LO, ORB_RATE_HI)

    def update(self, playerRect, player):
        orbEffects = []
        orbsListCopy = self.orbsList.copy()

        for oOrb in orbsListCopy:
            deleteMe = oOrb.update()
            if deleteMe:
                self.orbsList.remove(oOrb)
            elif oOrb.collide(playerRect):
                orbEffects.append(oOrb.orb_type)
                player.applyOrbEffect(oOrb.orb_type)
                self.orbsList.remove(oOrb)

        self.nFramesTilNextOrb -= 1
        if self.nFramesTilNextOrb <= 0:
            orb_type = random.choice([ORB_TYPE_SPEED, ORB_TYPE_SHIELD, ORB_TYPE_SLOW])
            newOrb = Orb(self.window, orb_type)
            self.orbsList.append(newOrb)
            self.nFramesTilNextOrb = random.randint(ORB_RATE_LO, ORB_RATE_HI)

        return orbEffects

    def draw(self):
        for oOrb in self.orbsList:
            oOrb.draw()
