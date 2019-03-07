from terrainBarrier import terrainBarrier

#entire terrain system needs to be redone, getTerrainAt is currently just bruteforcing

class world:
    def __init__(self, width, height):
        self.entities = []

        #terrible implementation of terrain
        self.terrain = []
        for i in range(0, width):
            self.terrain.append(terrainBarrier(0, i))
            self.terrain.append(terrainBarrier(height, i))
        for i in range(0, height):
            self.terrain.append(terrainBarrier(i, 0))
            self.terrain.append(terrainBarrier(i, width))

    def getTerrain(self):
        return self.terrain

    def getTerrainAt(self, posY, posX):
        for terrain in self.terrain:
            if terrain.getX() == posX and terrain.getY() == posY:
                return terrain

    def getEntity(self, UUID):
        for entity in self.entities:
            if entity.getUUID() == UUID:
                return entity

    def getEntities(self):
        return self.entities

    def addEntity(self, entity):
        self.entities.append(entity)

    def removeEntity(self, entity):
        self.entities.remove(entity)
