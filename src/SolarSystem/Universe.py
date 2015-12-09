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
        self.initPointLight()


    def initPointLight(self):
        plight = PointLight('plight')
        plight.setColor(VBase4(0.8, 0.8, 0.8, 1))
        plnp = render.attachNewNode(plight)
        plnp.setPos(0, 0, 3.8)
        render.setLight(plnp)


        plight2 = PointLight('plight')
        plight2.setColor(VBase4(0.8, 0.8, 0.8, 1))
        plnp2 = render.attachNewNode(plight2)
        plnp2.setPos(0, 0, -3.8)
        render.setLight(plnp2)

        plight3 = PointLight('plight')
        plight3.setColor(VBase4(0.8, 0.8, 0.8, 1))
        plnp3 = render.attachNewNode(plight3)
        plnp3.setPos(3.8, 0, 0)
        render.setLight(plnp3)

        plight4 = PointLight('plight')
        plight4.setColor(VBase4(0.8, 0.8, 0.8, 1))
        plnp4 = render.attachNewNode(plight4)
        plnp4.setPos(-3.8, 0, 0)
        render.setLight(plnp4)

        plight5 = PointLight('plight')
        plight5.setColor(VBase4(0.8, 0.8, 0.8, 1))
        plnp5 = render.attachNewNode(plight5)
        plnp5.setPos(0, -3.8, 0)
        render.setLight(plnp5)

        plight6 = PointLight('plight')
        plight6.setColor(VBase4(0.8, 0.8, 0.8, 1))
        plnp6 = render.attachNewNode(plight6)
        plnp6.setPos(0, 3.8, 0)
        render.setLight(plnp6)
        #render.setShaderAuto()
        base.setBackgroundColor(0, 0, 0)
        base.cam.lookAt(0, 0, 0)

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




