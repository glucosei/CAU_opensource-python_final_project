class PlayerStatusBar:
    def __init__(self,w):
        self.w = w
        self.player = self.w.data.player
        self.playerWidth = self.player.width
        self.playerHeight = self.player.height
        self.maxHpId = w.newRectangle((800/2)-200,950-50,400,50, fill_color='gray')
        self.currentHpId = w.newRectangle((800/2)-200,950-50,400,50, fill_color='red')
        self.textId = w.newText((800/2),950-25,width = 400,text=self._getText(), fill_color='black', anchor='center')

    def _getText(self):
        return f"HP: {int(self.player.hp)} / {int(self.player.MAX_HP)}"

    def update(self):
        self.w.raiseObject(self.maxHpId)
        self.w.raiseObject(self.currentHpId)
        self.w.raiseObject(self.textId)

        hpRatio = max(self.player.hp / self.player.MAX_HP, 0)
        hpRatio = min(hpRatio, 1)
        #print(hpRatio)
        self.w.resizeObject(self.currentHpId, hpRatio*400, 50)

        self.w.setText(self.textId, self._getText())