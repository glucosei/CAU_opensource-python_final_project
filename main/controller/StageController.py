from main.controller import EnemyController


class StageController:
    def __init__(self, w):
        self.w = w
        self.stage = 1
        self.countFrame = 0
        self.enemyController = EnemyController(w)


    def update(self):
        self.countFrame += 1
        if self.countFrame % (60*30) == 0:
            self.stage += 1

        if self.stage == 1:
            self.enemyController.stageOneUpdate()
            #(self.countFrame)