from panda3d.core import NodePath, TextNode
from direct.gui.DirectGui import *
import sys


class Sun(object):
    def __init__(self, sizescale):
        self.sizescale = sizescale

    def loadPlanet(self):
        self.sky = loader.loadModel("../../models/solar_sky_sphere")
        self.sky.reparentTo(render)
        self.sky.setScale(40)
        self.sky_tex = loader.loadTexture("../../models/stars_1k_tex.jpg")
        self.sky.setTexture(self.sky_tex, 1)
        self.sun = loader.loadModel("../../models/planet_sphere")
        self.sun.reparentTo(render)
        self.sun_tex = loader.loadTexture("../../models/sun_1k_tex.jpg")
        self.sun.setTexture(self.sun_tex, 1)
        self.sun.setScale(2 * self.sizescale)