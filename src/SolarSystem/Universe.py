from direct.showbase.ShowBase import ShowBase

from panda3d.core import *  # Contains most of Panda's modules
from direct.gui.DirectGui import *  # Imports Gui objects we use for putting
# text on the screen
import sys


class Universe(object):
    '''
        Klasse Universe
    '''
    def __init__(self, base):
        '''
        Klasse Konstruktor

        :param base: ShowBase from direct.showbase.ShowBase

        :return:
        '''
        self.base = base


    def initSky(self):
        # Load the model for the sky
        self.sky = loader.loadModel("../../models/solar_sky_sphere")
        # Load the texture for the sky.
        self.sky_tex = loader.loadTexture("../../models/stars_1k_tex.jpg")
        # Set the sky texture to the sky model
        self.sky.setTexture(self.sky_tex, 1)
        # Parent the sky model to the render node so that the sky is rendered
        self.sky.reparentTo(render)
        # Scale the size of the sky.
        self.sky.setScale(40)

    def displayOverlay(self):
        '''
        Displays a Overlay text in the bottom corner right

        :return:
        '''
        # Create some text overlayed on our screen.
        # We will use similar commands in all of our tutorials to create titles and
        # instruction guides.
        self.title = OnscreenText(
            text="Fock & Polydor - Solar System",
            parent=base.a2dBottomRight, align=TextNode.A_right,
            style=1, fg=(1, 1, 1, 1), pos=(-0.1, 0.1), scale=.07)

        # Make the background color black (R=0, G=0, B=0)
        # instead of the default grey
        base.setBackgroundColor(0, 0, 0)




