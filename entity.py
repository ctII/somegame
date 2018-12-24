import uuid


class entity:
    def __init__(self, world, posX, posY, form):
        self.world = world
        self.posX = posX
        self.posY = posY
        self.form = form
        self.uuid = uuid.uuid4()

    def getWorld(self):
        return self.world

    def setX(self, x):
        self.posX = x

    def setY(self, y):
        self.posY = y

    def getX(self):
        return self.posX

    def getY(self):
        return self.posY

    def getForm(self):
        return self.form

    def tick(self):
        pass

    def getUUID(self):
        return self.uuid
