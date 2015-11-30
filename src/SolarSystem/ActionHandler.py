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
        self.skeyEventText = 0
        self.ykeyEventText = 0
        self.vkeyEventText = 0
        self.ekeyEventText = 0
        self.mkeyEventText = 0
        self.speedUpText = 0
        self.slowDownText = 0

        self.simRunning = True
        self.instruction = 0
        self.origTex = True

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
        self.instructionText = self.genLabelText("[T]: Toggle Texture", 1)
        self.spaceKeyEventText = self.genLabelText(
            "[SPACE]: Toggle entire Solar System", 2)
        #self.skeyEventText = self.genLabelText("Sun [RUNNING]", 3)
        #self.ykeyEventText = self.genLabelText("Mercury [RUNNING]", 4)
        #self.vkeyEventText = self.genLabelText("Venus [RUNNING]", 5)
        #self.ekeyEventText = self.genLabelText("[E]: Toggle Earth [RUNNING]", 6)
        #self.mkeyEventText = self.genLabelText("Mars [RUNNING]", 7)
        self.speedUpText = self.genLabelText("[J] SPEED UP!", 3)
        self.slowDownText = self.genLabelText("[K] slow down...", 4)

        self.instruction = True

    '''
    def hideLayoutAction(self):
        self.instructionText = self.genLabelText("", 1)
        self.spaceKeyEventText = self.genLabelText(
            "", 2)
        #self.skeyEventText = self.genLabelText("Sun [RUNNING]", 3)
        #self.ykeyEventText = self.genLabelText("Mercury [RUNNING]", 4)
        #self.vkeyEventText = self.genLabelText("Venus [RUNNING]", 5)
        #self.ekeyEventText = self.genLabelText("[E]: Toggle Earth [RUNNING]", 6)
        #self.mkeyEventText = self.genLabelText("Mars [RUNNING]", 7)
        self.speedUpText = ""
        self.slowDownText = ""

        self.instructionText = self.genLabelText("[I]: Show Instruction", 1)
        self.instruction = False
    '''

    def activateAction(self):
        self.accept("escape", sys.exit)
        self.accept("e", self.handleEarth)
        self.accept("space", self.handleAll)
        self.accept("j", self.speedUp)
        self.accept("k", self.slowDown)
        self.accept("t", self.toggleTex)

    def toggleInstructions(self):
        if self.instruction == True:
            self.hideLayoutAction()
        else:
            self.displayLayout()

    def speedUp(self):
        print ("SpeedUP")

    def slowDown(self):
        print ("SlowDown")

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
                                  self.cbAttDic["jupiterOrbit"], self.mkeyEventText)
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
        #if day.isPlaying():
        #    print("Pausing " + planet)
        #    state = " [PAUSED]"
        #else:
        #    print("Resuming " + planet)
        #    state = " [RUNNING]"

        # Update the onscreen text if it is given as an argument
        #if text:
        #    old = text.getText()
            # strip out the last segment of text after the last white space
            # and append the string stored in 'state'
        #    text.setText(old[0:old.rfind(' ')] + state)

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

