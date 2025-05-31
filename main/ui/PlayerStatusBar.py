class PlayerStatusBar:
    def __init__(self,w):
        self.w = w
        self.player = self.w.data.player
        self.playerWidth = self.player.width
        self.playerHeight = self.player.height
        self.maxHpId = w.newRectangle((800/2)-200,950-50,400,50, fill_color='gray')
        self.currentHpId = w.newRectangle((800/2)-200,950-50,400,50, fill_color='red')

    def update(self):
        self.w.raiseObject(self.maxHpId)
        self.w.raiseObject(self.currentHpId)
        self.w.resizeObject(self.currentHpId, (self.player.hp/self.player.MAX_HP)*400, 50)