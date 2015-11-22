class Earth(object):
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
        self.orbit_root_earth = render.attachNewNode('orbit_root_earth')
        # Load earth
        self.earth = loader.loadModel("../../models/planet_sphere")
        self.earth_tex = loader.loadTexture("../../models/earth_1k_tex.jpg")
        self.earth.setTexture(self.earth_tex, 1)
        self.earth.reparentTo(self.orbit_root_earth)
        self.earth.setScale(self.sizescale)
        self.earth.setPos(self.orbitscale, 0, 0)

        # orbit_root_moon is like all the other orbit_root dummy nodes except that
        # it will be parented to orbit_root_earth so that the moon will orbit the
        # earth instead of the sun. So, the moon will first inherit
        # orbit_root_moon's position and then orbit_root_earth's. There is no hard
        # limit on how many objects can inherit from each other.
        self.orbit_root_moon = (
            self.orbit_root_earth.attachNewNode('orbit_root_moon'))

        # The center of the moon's orbit is exactly the same distance away from
        # The sun as the Earth's distance from the sun
        self.orbit_root_moon.setPos(self.orbitscale, 0, 0)

        # Load the moon
        self.moon = loader.loadModel("../../models/planet_sphere")
        self.moon_tex = loader.loadTexture("../../models/moon_1k_tex.jpg")
        self.moon.setTexture(self.moon_tex, 1)
        self.moon.reparentTo(self.orbit_root_moon)
        self.moon.setScale(0.1 * self.sizescale)
        self.moon.setPos(0.1 * self.orbitscale, 0, 0)

    def rotatePlanets(self):
        # earth
        self.orbit_period_earth = self.orbit_root_earth.hprInterval(
            self.yearscale, (360, 0, 0))
        self.day_period_earth = self.earth.hprInterval(
            self.dayscale, (360, 0, 0))

        # moon
        self.orbit_period_moon = self.orbit_root_moon.hprInterval(
            (.0749 * self.yearscale), (360, 0, 0))
        self.day_period_moon = self.moon.hprInterval(
            (.0749 * self.yearscale), (360, 0, 0))

        self.orbit_period_earth.loop()
        self.day_period_earth.loop()
        self.orbit_period_moon.loop()
        self.day_period_moon.loop()