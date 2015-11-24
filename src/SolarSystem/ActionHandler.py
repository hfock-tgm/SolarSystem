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
    def __init__(self, base, cbAtt, cbAttDic):
        DirectObject.__init__(self)
        self.base = base
        self.cbAtt = cbAtt
        self.cbAttDic = cbAttDic

        self.spaceKeyEventText = self.genLabelText(
            "SPACE: Toggle entire Solar System [RUNNING]", 1)
        self.skeyEventText = self.genLabelText("[S]: Toggle Sun [RUNNING]", 2)
        self.ykeyEventText = self.genLabelText("[Y]: Toggle Mercury [RUNNING]", 3)
        self.vkeyEventText = self.genLabelText("[V]: Toggle Venus [RUNNING]", 4)
        self.ekeyEventText = self.genLabelText("[E]: Toggle Earth [RUNNING]", 5)
        self.mkeyEventText = self.genLabelText("[M]: Toggle Mars [RUNNING]", 6)
        self.yearCounterText = self.genLabelText("0 Earth years completed", 7)
        self.text = self.genLabelText("Test", 8)

        self.yearCounter = 0  # year counter for earth years
        self.simRunning = True

    def displayLayout(self):
        self.title = OnscreenText(
            text="Fock & Polydor - SolarSystem",
            parent=base.a2dBottomRight, align=TextNode.A_right,
            style=1, fg=(1, 1, 1, 1), pos=(-0.1, 0.1), scale=.07)

    def activateAction(self):
        self.accept("escape", sys.exit)
        self.accept("e", self.handleEarth)
        self.accept("space", self.handleAll)

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
            # changing the text to reflect the change from "RUNNING" to
            # "PAUSED"
            self.spaceKeyEventText.setText(
                "SPACE: Toggle entire Solar System [PAUSED]")
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
        else:
            #"The simulation is paused, so resume it
            print("Resuming Simulation")
            self.spaceKeyEventText.setText(
                "SPACE: Toggle entire Solar System [RUNNING]")
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
        # toggle self.simRunning
        self.simRunning = not self.simRunning
    # end handleMouseClick

    def togglePlanet(self, planet, day, orbit=None, text=None):
        if day.isPlaying():
            print("Pausing " + planet)
            state = " [PAUSED]"
        else:
            print("Resuming " + planet)
            state = " [RUNNING]"

        # Update the onscreen text if it is given as an argument
        if text:
            old = text.getText()
            # strip out the last segment of text after the last white space
            # and append the string stored in 'state'
            text.setText(old[0:old.rfind(' ')] + state)

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
