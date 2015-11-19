
class Mercury(object):
    def __init__(self, sizescale, orbitscale):
        self.sizescale = sizescale
        self.orbitscale = orbitscale

    def loadPlanet(self):
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