from main.controller import EnemyController
from main.controller.StageNotifier import StageNotifier
from main.entity import Player
from main.ui.GameResult import GameResult
from main.ui.PlayerStatusBar import PlayerStatusBar
from main.ui.StartMenu import StartMenu


class StageController:
    def __init__(self, w):
        self.w = w
        self.stage = 0
        self.countFrame = 0
        self.enemyController = EnemyController(w)
        self.stageNotifier = StageNotifier(w)
        self.startMenu = StartMenu(w)
        self.gameResult = GameResult(w)

    def update(self):

        if self.w.data.player.hp <= 0 and self.stage != 11:
            self.stage = 11
            self.gameResult.overGame()
            return

        if self.stage == 0:
            startMenuReturn = self.startMenu.update()
            if startMenuReturn == 'start':
                self.stageNotifier.changeStage(1)
                self.stage += 1
            return


        if self.stage == 11:
            gameResultReturn = self.gameResult.update()
            if gameResultReturn == 'mainMenu':
                self.w.data.player.hp = self.w.data.player.MAX_HP
                self.stage = 0
                self.startMenu.show()
                for enemy in self.w.data.enemyList[:]:
                    enemy.onDeath()
                for bullet in self.w.data.bulletList[:]:
                    bullet.onDeath()

                print(self.w.data.enemyList, self.w.data.bulletList)
                self.w.deleteObject(self.w.data.player.id)
                self.w.data.player = Player(self.w,(self.w.data.width/2)-25,750,60,60,10)
                self.w.data.player.playerStatusBar = PlayerStatusBar(self.w)
            return

        self.countFrame += 1

        if self.countFrame % (60*30) == 0 and self.stage < 10:
            self.stage = min(10,self.stage+1)
            self.w.data.player.hp = min(self.w.data.player.hp + 50, self.w.data.player.MAX_HP)
            self.stageNotifier.changeStage(self.stage)


            match self.stage:
                case 1:
                    self.enemyController.stageOneStart()
                case 2:
                    self.enemyController.stageTwoStart()

                case 3:
                    self.enemyController.stageThreeStart()

                case 4:
                    self.enemyController.stageFourStart()

                case 5:
                    self.enemyController.stageFiveStart()

                case 6:
                    self.enemyController.stageSixStart()

                case 7:
                    self.enemyController.stageSevenStart()

                case 8:
                    self.enemyController.stageEightStart()

                case 9:
                    self.enemyController.stageNineStart()

                case 10:
                    self.enemyController.stageTenStart()


        match self.stage:
            case 1:
                self.enemyController.stageOneUpdate()
                
            case 2:
                self.enemyController.stageTwoUpdate()
                
            case 3:
                self.enemyController.stageThreeUpdate()
            
            case 4:
                self.enemyController.stageFourUpdate()
                
            case 5:
                self.enemyController.stageFiveUpdate()
                
            case 6:
                self.enemyController.stageSixUpdate()
                
            case 7:
                self.enemyController.stageSevenUpdate()
                
            case 8:
                self.enemyController.stageEightUpdate()
                
            case 9:
                self.enemyController.stageNineUpdate()
                
            case 10:
                self.enemyController.stageTenUpdate()
            