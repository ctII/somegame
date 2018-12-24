from entity import entity


class entityTest(entity):
    def __init__(self, world, posX, posY):
        entity.__init__(self, world, posX, posY, 'T')
        self.up = False

    def tick(self):
        if self.up is True:
            if self.posY is not 10:
                self.posY += 1
            else:
                self.posY -= 1
                self.up = False
        else:
            if self.posY is not 1:
                self.posY -= 1
            else:
                self.posY += 1
                self.up = True
        pass
