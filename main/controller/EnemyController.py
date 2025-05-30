
from main.controller.EnemySpawner import EnemySpawner


class EnemyController:
    def __init__(self,w):
        self.w = w
        self.spawnCooldown = 0
        self.SPAWN_COOLTIME = 60*10
        self.enemySpawner = EnemySpawner(w)

    def startStageOne(self):
        self.SPAWN_COOLTIME = 60*10
        self.enemySpawner.stageOneSpawn()

    def stageOneUpdate(self):

        if self.spawnCooldown <= 0:
            self.enemySpawner.stageOneSpawn()
            self.spawnCooldown = self.SPAWN_COOLTIME

        else:
            self.spawnCooldown -= 1

        for enemy in self.w.data.enemyList:
            enemy.update()


