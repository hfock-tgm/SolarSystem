from direct.showbase.ShowBase import ShowBase
import Universe
import Sun
import Mercury
import CameraHandler

sizescale = 0.6
orbitscale = 10

base = ShowBase()

camera = CameraHandler.CameraHandler(base)

u = Universe.Universe(base)
u.displayOverlay()


sun = Sun.Sun(sizescale)
sun.loadPlanet()


mer = Mercury.Mercury(sizescale, orbitscale)
mer.loadPlanet()


base.run()