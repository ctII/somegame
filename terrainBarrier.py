from terrain import terrain

class terrainBarrier(terrain):
    def __init__(self, x, y):
        super(terrainBarrier, self).__init__("B", x, y)
