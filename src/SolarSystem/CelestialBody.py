class CelestialBody(object):
    def __init__(self, sizescale, orbitscale, yearscale, dayscale):
        self.sizescale = sizescale
        self.orbitscale = orbitscale
        self.dayscale = dayscale
        self.yearscale = yearscale

        self.cbAtt = []
        self.cbAttDic = {}

    def loadAllCelestialBodys(self):
        self.loadSun()
        self.loadMercury()
        self.loadVenus()
        self.loadEarth()
        self.loadMoon()
        self.loadMars()
        self.loadJupiter()

    def rotateAllCelestialBodys(self):
        self.rotateSun()
        self.rotateMercury()
        self.rotateVenus()
        self.rotateEarth()
        self.rotateMoon()
        self.rotateMars()
        self.rotateJupiter()


    def loadSun(self):
        # Hier wird die Form fuer die Sonne geladen
        # In diesem Fall ist eine planet_sphere
        self.sun = loader.loadModel("../../models/planet_sphere")
        # Hier wird die Sonne ins Zentrum des SolarSystems platziert
        self.sun.reparentTo(render)
        # Hier wird der Sonne die gelbe Sonnen Textur geladen
        self.sun_tex = loader.loadTexture("../../models/sun_1k_tex.jpg")
        # Hier wird die Textur gesetzt
        self.sun.setTexture(self.sun_tex, 1)
        # Hier wird die Groesse des Himmelskoerper gesetzt
        self.sun.setScale(2 * self.sizescale)
    # end loadSun

    def rotateSun(self):
        # rotatePlanets creates intervals to actually use the hierarchy we created
        # to turn the sun, planets, and moon to give a rough representation of the
        # solar system. The next lesson will go into more depth on intervals.
        self.day_period_sun = self.sun.hprInterval(20, (360, 0, 0))
        self.day_period_sun.loop()
        self.cbAtt.append(self.day_period_sun)
        self.cbAttDic["sunDay"] = self.day_period_sun
    # end rotateSun

    def loadEarth(self):
        #Hier wird die Erde an die Sonne/render (den Mittelpunkt) angehaengt
        self.orbit_root_earth = render.attachNewNode('orbit_root_earth')
        # Load earth
        self.earth = loader.loadModel("../../models/planet_sphere")
        self.earth_tex = loader.loadTexture("../../models/earth_1k_tex.jpg")
        self.earth.setTexture(self.earth_tex, 1)
        self.earth.reparentTo(self.orbit_root_earth)
        self.earth.setScale(self.sizescale)
        self.earth.setPos(self.orbitscale, 0, 0)
    # end loadEarth

    def rotateEarth(self):
        # earth
        self.orbit_period_earth = self.orbit_root_earth.hprInterval(
            self.yearscale, (360, 0, 0))
        self.day_period_earth = self.earth.hprInterval(
            self.dayscale, (360, 0, 0))

        self.orbit_period_earth.loop()
        self.day_period_earth.loop()

        self.cbAtt.append(self.orbit_period_earth)
        self.cbAtt.append(self.day_period_earth)

        self.cbAttDic["earthDay"] = self.day_period_earth
        self.cbAttDic["earthOrbit"] = self.orbit_period_earth



    def loadMoon(self):
        # Hier wird der Mond an die Erde gehaengt
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

    def rotateMoon(self):
        # moon
        self.orbit_period_moon = self.orbit_root_moon.hprInterval(
            (.0749 * self.yearscale), (360, 0, 0))
        self.day_period_moon = self.moon.hprInterval(
            (.0749 * self.yearscale), (360, 0, 0))

        self.orbit_period_moon.loop()
        self.day_period_moon.loop()

        self.cbAtt.append(self.orbit_period_moon)
        self.cbAtt.append(self.day_period_moon)

        self.cbAttDic["moonDay"] = self.day_period_moon
        self.cbAttDic["moonOrbit"] = self.orbit_period_moon

    def loadMars(self):
        self.orbit_root_mars = render.attachNewNode("orbit_root_mars")

        # Load Mars
        self.mars = loader.loadModel("../../models/planet_sphere")
        self.mars_tex = loader.loadTexture("../../models/mars_1k_tex.jpg")
        self.mars.setTexture(self.mars_tex, 1)
        self.mars.reparentTo(self.orbit_root_mars)
        self.mars.setPos(1.52 * self.orbitscale, 0, 0)
        self.mars.setScale(0.515 * self.sizescale)

    def rotateMars(self):
        self.orbit_period_mars = self.orbit_root_mars.hprInterval(
            (1.881 * self.yearscale), (360, 0, 0))
        self.day_period_mars = self.mars.hprInterval(
            (1.03 * self.dayscale), (360, 0, 0))

        self.orbit_period_mars.loop()
        self.day_period_mars.loop()

        self.cbAtt.append(self.orbit_period_mars)
        self.cbAtt.append(self.day_period_mars)

        self.cbAttDic["marsDay"] = self.day_period_mars
        self.cbAttDic["marsOrbit"] = self.orbit_period_mars

    def loadMercury(self):
        self.orbit_root_mercury = render.attachNewNode('orbit_root_mercury')
        # Load mercury
        self.mercury = loader.loadModel("../../models/planet_sphere")
        self.mercury_tex = loader.loadTexture("../../models/mercury_1k_tex.jpg")
        self.mercury.setTexture(self.mercury_tex, 1)
        self.mercury.reparentTo(self.orbit_root_mercury)
        self.mercury.setPos(0.38 * self.orbitscale, 0, 0)
        self.mercury.setScale(0.385 * self.sizescale)

    def rotateMercury(self):
        self.orbit_period_mercury = self.orbit_root_mercury.hprInterval(
            (0.241 * self.yearscale), (360, 0, 0))
        self.day_period_mercury = self.mercury.hprInterval(
            (59 * self.dayscale), (360, 0, 0))

        self.orbit_period_mercury.loop()
        self.day_period_mercury.loop()

        self.cbAtt.append(self.orbit_period_mercury)
        self.cbAtt.append(self.day_period_mercury)

        self.cbAttDic["mercuryDay"] = self.day_period_mercury
        self.cbAttDic["mercuryOrbit"] = self.orbit_period_mercury

    def loadVenus(self):
        self.orbit_root_venus = render.attachNewNode('orbit_root_venus')

        # Load Venus
        self.venus = loader.loadModel("../../models/planet_sphere")
        self.venus_tex = loader.loadTexture("../../models/venus_1k_tex.jpg")
        self.venus.setTexture(self.venus_tex, 1)
        self.venus.reparentTo(self.orbit_root_venus)
        self.venus.setPos(0.72 * self.orbitscale, 0, 0)
        self.venus.setScale(0.923 * self.sizescale)

    def rotateVenus(self):
        self.orbit_period_venus = self.orbit_root_venus.hprInterval(
            (0.615 * self.yearscale), (360, 0, 0))
        self.day_period_venus = self.venus.hprInterval(
            (243 * self.dayscale), (360, 0, 0))

        self.orbit_period_venus.loop()
        self.day_period_venus.loop()

        self.cbAtt.append(self.orbit_period_venus)
        self.cbAtt.append(self.day_period_venus)

        self.cbAttDic["venusDay"] = self.day_period_venus
        self.cbAttDic["venusOrbit"] = self.orbit_period_venus

    def loadJupiter(self):
        self.orbit_root_jupiter = render.attachNewNode('orbit_root_jupiter')

        # Load jupiter
        self.jupiter = loader.loadModel("../../models/planet_sphere")
        self.jupiter_tex = loader.loadTexture("../../models/jupiter.jpg")
        self.jupiter.setTexture(self.jupiter_tex, 1)
        self.jupiter.reparentTo(self.orbit_root_jupiter)
        self.jupiter.setPos(2 * self.orbitscale, 0, 0)
        self.jupiter.setScale(0.923 * self.sizescale)

    def rotateJupiter(self):
        self.orbit_period_jupiter = self.orbit_root_jupiter.hprInterval(
            (3 * self.yearscale), (360, 0, 0))
        self.day_period_jupiter = self.jupiter.hprInterval(
            (23 * self.dayscale), (360, 0, 0))

        self.orbit_period_jupiter.loop()
        self.day_period_jupiter.loop()

        self.cbAtt.append(self.orbit_period_jupiter)
        self.cbAtt.append(self.day_period_jupiter)

        self.cbAttDic["jupiterDay"] = self.day_period_jupiter
        self.cbAttDic["jupiterOrbit"] = self.orbit_period_jupiter
