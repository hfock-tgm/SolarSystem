from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject

import CameraHandler
import Universe
import CelestialBody
import ActionHandler

class Main(DirectObject):
    sizescale = 0.6
    orbitscale = 10
    yearscale = 60
    dayscale = yearscale / 365.0 * 5

    base = ShowBase()

    camera = CameraHandler.CameraHandler(base)

    u = Universe.Universe(base)
    u.initSky()

    cb = CelestialBody.CelestialBody(sizescale, orbitscale, yearscale, dayscale)
    cb.loadAllCelestialBodys()
    cb.rotateAllCelestialBodys()

    action = ActionHandler.ActionHandler(base, cb.cbAtt, cb.cbAttDic, cb.cbAttTex)
    action.initAll()


    base.run()