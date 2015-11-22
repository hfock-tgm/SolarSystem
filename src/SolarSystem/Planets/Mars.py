class Mars(object):
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
        self.orbit_root_mars = render.attachNewNode("orbit_root_mars")

        # Load Mars
        self.mars = loader.loadModel("../../models/planet_sphere")
        self.mars_tex = loader.loadTexture("../../models/mars_1k_tex.jpg")
        self.mars.setTexture(self.mars_tex, 1)
        self.mars.reparentTo(self.orbit_root_mars)
        self.mars.setPos(1.52 * self.orbitscale, 0, 0)
        self.mars.setScale(0.515 * self.sizescale)

    def rotatePlanets(self):
        self.orbit_period_mars = self.orbit_root_mars.hprInterval(
            (1.881 * self.yearscale), (360, 0, 0))
        self.day_period_mars = self.mars.hprInterval(
            (1.03 * self.dayscale), (360, 0, 0))

        self.orbit_period_mars.loop()
        self.day_period_mars.loop()