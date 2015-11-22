class Venus(object):
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
        self.orbit_root_venus = render.attachNewNode('orbit_root_venus')

        # Load Venus
        self.venus = loader.loadModel("../../models/planet_sphere")
        self.venus_tex = loader.loadTexture("../../models/venus_1k_tex.jpg")
        self.venus.setTexture(self.venus_tex, 1)
        self.venus.reparentTo(self.orbit_root_venus)
        self.venus.setPos(0.72 * self.orbitscale, 0, 0)
        self.venus.setScale(0.923 * self.sizescale)

    def rotatePlanets(self):
        self.orbit_period_venus = self.orbit_root_venus.hprInterval(
            (0.615 * self.yearscale), (360, 0, 0))
        self.day_period_venus = self.venus.hprInterval(
            (243 * self.dayscale), (360, 0, 0))

        self.orbit_period_venus.loop()
        self.day_period_venus.loop()
