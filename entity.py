import uuid


class entity:
    def __init__(self, posX, posY, form):
        self.posX = posX
        self.posY = posY
        self.form = form
        self.uuid = uuid.uuid4()

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
