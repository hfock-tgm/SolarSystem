
class Mercury(object):
    def __init__(self, sizescale, orbitscale, yearscale, dayscale):
        self.sizescale = sizescale
        self.orbitscale = orbitscale
        self.dayscale = dayscale
        self.yearscale = yearscale

    def loadPlanet(self):
        # We do this because positioning the planets around a circular orbit could
        # be done with a lot of messy sine and cosine operations. Instead, we define
        # our planets to be a given distance from a dummy node, and when we turn the
        # dummy, the planets will move along with it, kind of like turning the
        # center of a disc and having an object at its edge move. Most attributes,
        # like position, orientation, scale, texture, color, etc., are inherited
        # this way. Panda deals with the fact that the objects are not attached
        # directly to render (they are attached through other NodePaths to render),
        # and makes sure the attributes inherit.

        # This system of attaching NodePaths to each other is called the Scene
        # Graph
        self.orbit_root_mercury = render.attachNewNode('orbit_root_mercury')
        # Load mercury
        self.mercury = loader.loadModel("../../models/planet_sphere")
        self.mercury_tex = loader.loadTexture("../../models/mercury_1k_tex.jpg")
        self.mercury.setTexture(self.mercury_tex, 1)
        self.mercury.reparentTo(self.orbit_root_mercury)
        # Set the position of mercury. By default, all nodes are pre assigned the
        # position (0, 0, 0) when they are first loaded. We didn't reposition the
        # sun and sky because they are centered in the solar system. Mercury,
        # however, needs to be offset so we use .setPos to offset the
        # position of mercury in the X direction with respect to its orbit radius.
        # We will do this for the rest of the planets.
        self.mercury.setPos(0.38 * self.orbitscale, 0, 0)
        self.mercury.setScale(0.385 * self.sizescale)

    def rotatePlanets(self):
        self.orbit_period_mercury = self.orbit_root_mercury.hprInterval(
            (0.241 * self.yearscale), (360, 0, 0))
        self.day_period_mercury = self.mercury.hprInterval(
            (59 * self.dayscale), (360, 0, 0))

        self.orbit_period_mercury.loop()
        self.day_period_mercury.loop()