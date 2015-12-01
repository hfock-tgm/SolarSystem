class CameraHandler(object):
    def __init__(self, base):


        #base.disableMouse()
        self.base = base
        camera.setPos(0, 0, 45)
        camera.setHpr(0, -90, 0)
        self.base.trackball.node().setPos(0, 60, 0)