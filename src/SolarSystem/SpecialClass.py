from direct.particles.Particles import Particles
from direct.particles.ParticleEffect import ParticleEffect
from panda3d.core import AmbientLight, DirectionalLight
from panda3d.core import LPoint3, LVector3
from panda3d.core import Filename

class SpecialClass(object):
    def __init__(self, base, sun):
        self.base = base
        self.sun = sun
        # This command is required for Panda to render particles
        base.enableParticles()
        self.t = sun
        self.t.setPos(0, 0, 0)
        self.t.reparentTo(render)
        self.setupLights()
        self.p = ParticleEffect()
        self.loadParticleConfig('../../models/fireish.ptf')

    def loadParticleConfig(self, filename):
        # Start of the code from steam.ptf
        self.p.cleanup()
        self.p = ParticleEffect()
        self.p.loadConfig(Filename(filename))
        # Sets particles to birth relative to the teapot, but to render at
        # toplevel
        self.p.start(self.t)
        self.p.setPos(0.000, 0.000, 0.000)

    # Setup lighting
    def setupLights(self):
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.4, .4, .35, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(LVector3(0, 8, -2.5))
        directionalLight.setColor((0.9, 0.8, 0.9, 1))
        # Set lighting on teapot so steam doesn't get affected
        self.t.setLight(self.t.attachNewNode(directionalLight))
        self.t.setLight(self.t.attachNewNode(ambientLight))

    def initFIRE(self):
        pass