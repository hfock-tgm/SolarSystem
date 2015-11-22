from src.SolarSystem.Planets import Sun
from direct.showbase.ShowBase import ShowBase

import Planets.Earth
import Planets.Mercury
import Planets.Mars
import Planets.Venus
import CameraHandler
import Universe


sizescale = 0.6
orbitscale = 10
yearscale = 60
dayscale = yearscale / 365.0 * 5

base = ShowBase()

camera = CameraHandler.CameraHandler(base)

u = Universe.Universe(base)
u.displayOverlay()
u.initSky()

sun = Sun.Sun(sizescale)
sun.loadPlanet()
sun.rotatePlanets()

mer = Planets.Mercury.Mercury(sizescale, orbitscale, yearscale, dayscale)
mer.loadPlanet()
mer.rotatePlanets()

venus = Planets.Venus.Venus(sizescale, orbitscale, yearscale, dayscale)
venus.loadPlanet()
venus.rotatePlanets()

earth = Planets.Earth.Earth(sizescale, orbitscale, yearscale, dayscale)
earth.loadPlanet()
earth.rotatePlanets()

mars = Planets.Mars.Mars(sizescale, orbitscale, yearscale, dayscale)
mars.loadPlanet()
mars.rotatePlanets()

base.run()