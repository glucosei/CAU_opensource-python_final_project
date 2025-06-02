class StartMenu:
    def __init__(self,w):
        self.w = w
        self.MARGIN = 100
        self.titleId = w.newImage((w.data.width/2)-(498.6/2), self.MARGIN , "resource/title.png", int(498.6), int(159.9))
        self.startId = w.newImage((w.data.width/2)-(429/2), self.MARGIN +159.9+self.MARGIN , "resource/start.png", int(429), int(159.9))
        self.description = w.newImage((w.data.width/2)-(429.6/2), self.MARGIN +159.9+self.MARGIN +159.9+self.MARGIN , "resource/description.png", int(429), int(159.9))
        self.mouseHandler = self.w.data.mouseHandler

    def show(self):
        self.w.showObject(self.titleId)
        self.w.showObject(self.startId)
        self.w.showObject(self.description)

    def hide(self):
        self.w.hideObject(self.titleId)
        self.w.hideObject(self.startId)
        self.w.hideObject(self.description)

    def update(self):
        if self.mouseHandler.isJustPressed(1):
            x, y = self.mouseHandler.getPosition()
            if self.w.getTopObjectAt(x,y) == self.startId:
                self.hide()
                return 'start'
            elif self.w.getTopObjectAt(x,y) == self.description:
                self.hide()
                return 'description'
        return None


