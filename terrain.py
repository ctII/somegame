class terrain:
    def __init__(self, form, x, y):
        self.form = form
        self.posX = x
        self.posY = y
        
    def getForm(self):
        return self.form

    def getX(self):
        return self.posX

    def getY(self):
        return self.posY
