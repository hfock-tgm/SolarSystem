class CameraHandler(object):
    def __init__(self, base):
        self.base = base
        # By default, the mouse controls the camera. Often, we disable that so that
        # the camera can be placed manually (if we don't do this, our placement
        # commands will be overridden by the mouse control)
        base.disableMouse()
        # Set the camera position (x, y, z)
        camera.setPos(0, 0, 45)

        # Set the camera orientation (heading, pitch, roll) in degrees
        camera.setHpr(0, -90, 0)