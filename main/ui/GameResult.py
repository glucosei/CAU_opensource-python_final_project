class GameResult:
    def __init__(self,w):
        self.w = w
        self.mouseHandler = w.data.mouseHandler
        self.clear = w.newImage((w.data.width/2)-(429/2), w.data.height/3 , "resource/clear.png", int(429.0), int(230.2), isVisible=False)
        self.gameOver = w.newImage((w.data.width/2)-(455.0/2), w.data.height/3 , "resource/gameOver.png", int(455.0), int(159.9), isVisible=False)
        self.goToMainMenu = w.newImage((w.data.width/2)-(439.9/2), w.data.height*2/3 , "resource/goTOMainMenu.png", int(439.9), int(84.8), isVisible=False)

    def clearGame(self):
        self.w.showObject(self.clear)
        self.w.showObject(self.goToMainMenu)

    def overGame(self):
        self.w.showObject(self.gameOver)
        self.w.showObject(self.goToMainMenu)

    def update(self):
        if self.mouseHandler.isJustPressed(1):
            x,y = self.mouseHandler.getPosition()
            if self.w.getTopObjectAt(x,y) == self.goToMainMenu:
                self.w.hideObject(self.clear)
                self.w.hideObject(self.gameOver)
                self.w.hideObject(self.goToMainMenu)
                return 'mainMenu'
        return None