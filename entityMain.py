from entity import entity


class entityMain(entity):
    def __init__(self, world, posX, posY):
        entity.__init__(self, world, posX, posY, 'P')

    def moveUp(self):
        pass

    def moveDown(self):
        pass

    def moveRight(self):
        pass

    def moveLeft(self):
        pass
