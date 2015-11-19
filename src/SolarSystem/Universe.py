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



    def displayOverlay(self):
        '''

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




