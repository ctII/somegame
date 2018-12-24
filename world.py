class world:
    def __init__(self):
        self.entities = []

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
