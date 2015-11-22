from panda3d.core import NodePath, TextNode
from direct.gui.DirectGui import *
import sys


class Sun(object):
    def __init__(self, sizescale):
        self.sizescale = sizescale

    def loadPlanet(self):
        self.sun = loader.loadModel("../../models/planet_sphere")
        self.sun.reparentTo(render)
        self.sun_tex = loader.loadTexture("../../models/sun_1k_tex.jpg")
        self.sun.setTexture(self.sun_tex, 1)
        self.sun.setScale(2 * self.sizescale)
    # end loadPlanet

    def rotatePlanets(self):
        # rotatePlanets creates intervals to actually use the hierarchy we created
        # to turn the sun, planets, and moon to give a rough representation of the
        # solar system. The next lesson will go into more depth on intervals.
        self.day_period_sun = self.sun.hprInterval(20, (360, 0, 0))

        self.day_period_sun.loop()
    # end rotatePlanets