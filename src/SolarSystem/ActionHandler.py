from direct.showbase import DirectObject
from panda3d.core import TextNode
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
import sys

class ActionHandler(DirectObject):
    def genLabelText(self, text, i):
        return OnscreenText(text=text, pos=(0.06, -.06 * (i + 0.5)), fg=(1, 1, 1, 1),
                            parent=base.a2dTopLeft,align=TextNode.ALeft, scale=.05)

    def __init__(self, base, cbAtt, cbAttDic, cbAttTex):
        DirectObject.__init__(self)
        self.base = base
        self.cbAtt = cbAtt
        self.cbAttDic = cbAttDic
        self.cbAttTex = cbAttTex

        self.instructionText = 0
        self.spaceKeyEventText = 0
        self.speedUpText = 0
        self.slowDownText = 0

        self.simRunning = True
        self.instruction = True
        self.origTex = True

        self.instructionText = 0
        self.spaceKeyEventText = 0
        self.skeyEventText = 0
        self.ykeyEventText = 0
        self.vkeyEventText = 0
        self.ekeyEventText = 0
        self.mkeyEventText = 0
        self.jkeyEventText = 0
        self.speedUpText = 0
        self.slowDownText = 0
        self.toggleTextureText = 0
        self.resetSolarSystemText = 0

    def initAll(self):
        self.displayLayout()
        self.displayLayoutAction()
        self.activateAction()

    def displayLayout(self):
        self.title = OnscreenText(
            text="Fock & Polydor - SolarSystem",
            parent=base.a2dBottomRight, align=TextNode.A_right,
            style=1, fg=(1, 1, 1, 1), pos=(-0.1, 0.1), scale=.07)

    def displayLayoutAction(self):
        self.instructionText = self.genLabelText("[I]: Hide Instructions", 1)
        self.spaceKeyEventText = self.genLabelText("[SPACE]: Toggle entire Solar System", 2)
        self.speedUpText = self.genLabelText("[+]: SPEED UP!", 3)
        self.slowDownText = self.genLabelText("[-]: slow down...", 4)
        self.toggleTextureText = self.genLabelText("[T]: Toggle Texture", 5)
        self.resetSolarSystemText = self.genLabelText("[R]: Reset Solar System", 6)


    def hideLayoutAction(self):
        self.instructionText.hide()
        self.spaceKeyEventText.hide()
        self.speedUpText.hide()
        self.slowDownText.hide()
        self.toggleTextureText.hide()
        self.resetSolarSystemText.hide()

        self.instructionText = self.genLabelText("[I]: Show Instructions", 1)



    def activateAction(self):
        self.accept("escape", sys.exit)
        self.accept("e", self.handleEarth)
        self.accept("space", self.handleAll)
        self.accept("+", self.speedUp)
        self.accept("-", self.slowDown)
        self.accept("t", self.toggleTex)
        self.accept("i", self.toggleInstructions)
        self.accept("r", self.resetSolarSystem)

    def toggleInstructions(self):
        if self.instruction == True:
            print("True")
            self.hideLayoutAction()
            self.instruction = False
        elif self.instruction == False:
            print("False")
            self.displayLayout()
            self.instruction = True

    def speedUp(self):
        print ("SpeedUP")
        if (self.cbAttDic["sunDay"].getPlayRate() == -1):
            #sun
            self.cbAttDic["sunDay"].setPlayRate(1)
            #earth
            self.cbAttDic["earthOrbit"].setPlayRate(1)
            self.cbAttDic["earthDay"].setPlayRate(1)
            #moon
            self.cbAttDic["moonOrbit"].setPlayRate(1)
            self.cbAttDic["moonDay"].setPlayRate(1)
            #mars
            self.cbAttDic["marsOrbit"].setPlayRate(1)
            self.cbAttDic["marsDay"].setPlayRate(1)
            #mercury
            self.cbAttDic["mercuryOrbit"].setPlayRate(1)
            self.cbAttDic["mercuryDay"].setPlayRate(1)
            #jupiter
            self.cbAttDic["jupiterOrbit"].setPlayRate(1)
            self.cbAttDic["jupiterDay"].setPlayRate(1)
            #venus
            self.cbAttDic["venusOrbit"].setPlayRate(1)
            self.cbAttDic["venusDay"].setPlayRate(1)
        else:
            #sun
            self.cbAttDic["sunDay"].setPlayRate(self.cbAttDic["sunDay"].getPlayRate()+1)
            #earth
            self.cbAttDic["earthOrbit"].setPlayRate(self.cbAttDic["earthOrbit"].getPlayRate()+1)
            self.cbAttDic["earthDay"].setPlayRate(self.cbAttDic["earthDay"].getPlayRate()+1)
            #moon
            self.cbAttDic["moonOrbit"].setPlayRate(self.cbAttDic["moonOrbit"].getPlayRate()+1)
            self.cbAttDic["moonDay"].setPlayRate(self.cbAttDic["moonDay"].getPlayRate()+1)
            #mars
            self.cbAttDic["marsOrbit"].setPlayRate(self.cbAttDic["marsOrbit"].getPlayRate()+1)
            self.cbAttDic["marsDay"].setPlayRate(self.cbAttDic["marsDay"].getPlayRate()+1)
            #mercury
            self.cbAttDic["mercuryOrbit"].setPlayRate(self.cbAttDic["mercuryOrbit"].getPlayRate()+1)
            self.cbAttDic["mercuryDay"].setPlayRate(self.cbAttDic["mercuryDay"].getPlayRate()+1)
            #jupiter
            self.cbAttDic["jupiterOrbit"].setPlayRate(self.cbAttDic["jupiterOrbit"].getPlayRate()+1)
            self.cbAttDic["jupiterDay"].setPlayRate(self.cbAttDic["jupiterDay"].getPlayRate()+1)
            #venus
            self.cbAttDic["venusOrbit"].setPlayRate(self.cbAttDic["venusOrbit"].getPlayRate()+1)
            self.cbAttDic["venusDay"].setPlayRate(self.cbAttDic["venusDay"].getPlayRate()+1)




        print (self.cbAttDic["sunDay"].getPlayRate())


    def slowDown(self):
        print ("SlowDown")
        if (self.cbAttDic["sunDay"].getPlayRate() == 1):
            #sun
            self.cbAttDic["sunDay"].setPlayRate(-1)
            #earth
            self.cbAttDic["earthOrbit"].setPlayRate(-1)
            self.cbAttDic["earthDay"].setPlayRate(-1)
            #moon
            self.cbAttDic["moonOrbit"].setPlayRate(-1)
            self.cbAttDic["moonDay"].setPlayRate(-1)
            #mars
            self.cbAttDic["marsOrbit"].setPlayRate(-1)
            self.cbAttDic["marsDay"].setPlayRate(-1)
            #mercury
            self.cbAttDic["mercuryOrbit"].setPlayRate(-1)
            self.cbAttDic["mercuryDay"].setPlayRate(-1)
            #jupiter
            self.cbAttDic["jupiterOrbit"].setPlayRate(-1)
            self.cbAttDic["jupiterDay"].setPlayRate(-1)
            #venus
            self.cbAttDic["venusOrbit"].setPlayRate(-1)
            self.cbAttDic["venusDay"].setPlayRate(-1)
        else:
            #sun
            self.cbAttDic["sunDay"].setPlayRate(self.cbAttDic["sunDay"].getPlayRate()-1)
            #earth
            self.cbAttDic["earthOrbit"].setPlayRate(self.cbAttDic["earthOrbit"].getPlayRate()-1)
            self.cbAttDic["earthDay"].setPlayRate(self.cbAttDic["earthDay"].getPlayRate()-1)
            #moon
            self.cbAttDic["moonOrbit"].setPlayRate(self.cbAttDic["moonOrbit"].getPlayRate()-1)
            self.cbAttDic["moonDay"].setPlayRate(self.cbAttDic["moonDay"].getPlayRate()-1)
            #mars
            self.cbAttDic["marsOrbit"].setPlayRate(self.cbAttDic["marsOrbit"].getPlayRate()-1)
            self.cbAttDic["marsDay"].setPlayRate(self.cbAttDic["marsDay"].getPlayRate()-1)
            #mercury
            self.cbAttDic["mercuryOrbit"].setPlayRate(self.cbAttDic["mercuryOrbit"].getPlayRate()-1)
            self.cbAttDic["mercuryDay"].setPlayRate(self.cbAttDic["mercuryDay"].getPlayRate()-1)
            #jupiter
            self.cbAttDic["jupiterOrbit"].setPlayRate(self.cbAttDic["jupiterOrbit"].getPlayRate()-1)
            self.cbAttDic["jupiterDay"].setPlayRate(self.cbAttDic["jupiterDay"].getPlayRate()-1)
            #venus
            self.cbAttDic["venusOrbit"].setPlayRate(self.cbAttDic["venusOrbit"].getPlayRate()-1)
            self.cbAttDic["venusDay"].setPlayRate(self.cbAttDic["venusDay"].getPlayRate()-1)

        print (self.cbAttDic["sunDay"].getPlayRate())

    def handleEarth(self):
        self.togglePlanet("Earth", self.cbAttDic["earthDay"],
                          self.cbAttDic["earthOrbit"], self.ekeyEventText)
        self.togglePlanet("Moon", self.cbAttDic["moonDay"],
                          self.cbAttDic["moonOrbit"])
    # end handleEarth


    def handleAll(self):
        # When the mouse is clicked, if the simulation is running pause all the
        # planets and sun, otherwise resume it
        if self.simRunning:
            print("Pausing Simulation")
            # For each planet, check if it is moving and if so, pause it
            # Sun
            if self.cbAttDic["sunDay"].isPlaying():
                self.togglePlanet("Sun", self.cbAttDic["sunDay"], None,
                                  self.skeyEventText)
            if self.cbAttDic["mercuryDay"].isPlaying():
                self.togglePlanet("Mercury", self.cbAttDic["mercuryDay"],
                                  self.cbAttDic["mercuryOrbit"], self.ykeyEventText)
            # Venus
            if self.cbAttDic["venusDay"].isPlaying():
                self.togglePlanet("Venus", self.cbAttDic["venusDay"],
                                  self.cbAttDic["venusOrbit"], self.vkeyEventText)
            #Earth and moon
            if self.cbAttDic["earthDay"].isPlaying():
                self.togglePlanet("Earth", self.cbAttDic["earthDay"],
                                  self.cbAttDic["earthOrbit"], self.ekeyEventText)
                self.togglePlanet("Moon", self.cbAttDic["moonDay"],
                                  self.cbAttDic["moonOrbit"])
            # Mars
            if self.cbAttDic["marsDay"].isPlaying():
                self.togglePlanet("Mars", self.cbAttDic["marsDay"],
                                  self.cbAttDic["marsOrbit"], self.mkeyEventText)
            # jupiter
            if self.cbAttDic["jupiterDay"].isPlaying():
                self.togglePlanet("jupiter", self.cbAttDic["jupiterDay"],
                                  self.cbAttDic["jupiterOrbit"], self.jkeyEventText)
        else:
            #"The simulation is paused, so resume it
            print("Resuming Simulation")
            # the not operator does the reverse of the previous code
            if not self.cbAttDic["sunDay"].isPlaying():
                self.togglePlanet("Sun", self.cbAttDic["sunDay"], None,
                                  self.skeyEventText)
            if not self.cbAttDic["mercuryDay"].isPlaying():
                self.togglePlanet("Mercury", self.cbAttDic["mercuryDay"],
                                  self.cbAttDic["mercuryOrbit"], self.ykeyEventText)
            if not self.cbAttDic["venusDay"].isPlaying():
                self.togglePlanet("Venus", self.cbAttDic["venusDay"],
                                  self.cbAttDic["venusOrbit"], self.vkeyEventText)
            if not self.cbAttDic["earthDay"].isPlaying():
                self.togglePlanet("Earth", self.cbAttDic["earthDay"],
                                  self.cbAttDic["earthOrbit"], self.ekeyEventText)
                self.togglePlanet("Moon", self.cbAttDic["moonDay"],
                                  self.cbAttDic["moonOrbit"])
            if not self.cbAttDic["marsDay"].isPlaying():
                self.togglePlanet("Mars", self.cbAttDic["marsDay"],
                                  self.cbAttDic["marsOrbit"], self.mkeyEventText)
            if not self.cbAttDic["jupiterDay"].isPlaying():
                self.togglePlanet("jupiter", self.cbAttDic["jupiterDay"],
                                  self.cbAttDic["jupiterOrbit"], self.mkeyEventText)
        # toggle self.simRunning
        self.simRunning = not self.simRunning
    # end handleMouseClick

    def togglePlanet(self, planet, day, orbit=None, text=None):
        # toggle the day interval
        self.toggleInterval(day)
        # if there is an orbit interval, toggle it
        if orbit:
            self.toggleInterval(orbit)
    # end togglePlanet

    def toggleInterval(self, interval):
        if interval.isPlaying():
            interval.pause()
        else:
            interval.resume()
    # end toggleInterval

    def toggleTex(self):
        if (self.origTex == True):
            self.origTex = False

            # toggle sun
            self.cbAttTex["sunTex"] = loader.loadTexture("../../models/weiss.jpg")
            self.cbAttTex["sun"].setTexture(self.cbAttTex["sunTex"], 1)

            # toggle earth
            self.cbAttTex["earthTex"] = loader.loadTexture("../../models/weiss.jpg")
            self.cbAttTex["earth"].setTexture(self.cbAttTex["earthTex"], 1)

            # toggle moon
            self.cbAttTex["moonTex"] = loader.loadTexture("../../models/weiss.jpg")
            self.cbAttTex["moon"].setTexture(self.cbAttTex["moonTex"], 1)

            # toggle mars
            self.cbAttTex["marsTex"] = loader.loadTexture("../../models/weiss.jpg")
            self.cbAttTex["mars"].setTexture(self.cbAttTex["marsTex"], 1)

            # toggle mercury
            self.cbAttTex["mercuryTex"] = loader.loadTexture("../../models/weiss.jpg")
            self.cbAttTex["mercury"].setTexture(self.cbAttTex["mercuryTex"], 1)

            # toggle venus
            self.cbAttTex["venusTex"] = loader.loadTexture("../../models/weiss.jpg")
            self.cbAttTex["venus"].setTexture(self.cbAttTex["venusTex"], 1)

            # toggle jupiter
            self.cbAttTex["jupiterTex"] = loader.loadTexture("../../models/weiss.jpg")
            self.cbAttTex["jupiter"].setTexture(self.cbAttTex["jupiterTex"], 1)


        else:
            self.origTex = True
            # toggle sun
            self.cbAttTex["sunTex"] = loader.loadTexture("../../models/sun_1k_tex.jpg")
            self.cbAttTex["sun"].setTexture(self.cbAttTex["sunTex"], 1)

            # toggle earth
            self.cbAttTex["earthTex"] = loader.loadTexture("../../models/earth_1k_tex.jpg")
            self.cbAttTex["earth"].setTexture(self.cbAttTex["earthTex"], 1)

           # toggle moon
            self.cbAttTex["moonTex"] = loader.loadTexture("../../models/moon_1k_tex.jpg")
            self.cbAttTex["moon"].setTexture(self.cbAttTex["moonTex"], 1)

           # toggle mars
            self.cbAttTex["marsTex"] = loader.loadTexture("../../models/mars_1k_tex.jpg")
            self.cbAttTex["mars"].setTexture(self.cbAttTex["marsTex"], 1)

           # toggle mercury
            self.cbAttTex["mercuryTex"] = loader.loadTexture("../../models/mercury_1k_tex.jpg")
            self.cbAttTex["mercury"].setTexture(self.cbAttTex["mercuryTex"], 1)

           # toggle jupiter
            self.cbAttTex["jupiterTex"] = loader.loadTexture("../../models/jupiter.jpg")
            self.cbAttTex["jupiter"].setTexture(self.cbAttTex["jupiterTex"], 1)

           # toggle venus
            self.cbAttTex["venusTex"] = loader.loadTexture("../../models/venus_1k_tex.jpg")
            self.cbAttTex["venus"].setTexture(self.cbAttTex["venusTex"], 1)

    def resetSolarSystem(self):
        #sun
        self.cbAttDic["sunDay"].setPlayRate(0)
        #earth
        self.cbAttDic["earthOrbit"].setPlayRate(0)
        self.cbAttDic["earthDay"].setPlayRate(0)
        #moon
        self.cbAttDic["moonOrbit"].setPlayRate(0)
        self.cbAttDic["moonDay"].setPlayRate(0)
        #mars
        self.cbAttDic["marsOrbit"].setPlayRate(0)
        self.cbAttDic["marsDay"].setPlayRate(0)
        #mercury
        self.cbAttDic["mercuryOrbit"].setPlayRate(0)
        self.cbAttDic["mercuryDay"].setPlayRate(0)
        #jupiter
        self.cbAttDic["jupiterOrbit"].setPlayRate(0)
        self.cbAttDic["jupiterDay"].setPlayRate(0)
        #venus
        self.cbAttDic["venusOrbit"].setPlayRate(0)
        self.cbAttDic["venusDay"].setPlayRate(0)

