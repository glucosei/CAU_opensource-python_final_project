
from main.controller.EnemySpawner import EnemySpawner


class EnemyController:
    def __init__(self,w):
        self.w = w
        self.spawnCooldown = 0
        self.SPAWN_COOLTIME = 60*5
        self.enemySpawner = EnemySpawner(w)

    def stageOneStart(self):
        self.SPAWN_COOLTIME = 60*5
        self.enemySpawner.stageOneSpawn()

    def stageOneUpdate(self):


        if self.spawnCooldown <= 0:
            self.enemySpawner.stageOneSpawn()
            self.spawnCooldown = self.SPAWN_COOLTIME

        else:
            self.spawnCooldown -= 1

        enemysToRemove = []


        for enemy in self.w.data.enemyList:
            enemy.update()

            if enemy.y >= self.w.data.height:
                self.w.data.player.onHit(enemy.hp)
                enemysToRemove.append(enemy)

        for enemy in enemysToRemove:
            enemy.onDeath()

    def stageTwoStart(self):
        pass

    def stageTwoUpdate(self):
        if self.spawnCooldown <= 0:
            self.enemySpawner.stageTwoSpawn()
            self.spawnCooldown = self.SPAWN_COOLTIME

        else:
            self.spawnCooldown -= 1

        enemysToRemove = []

        for enemy in self.w.data.enemyList:
            enemy.update()
            if enemy.y >= self.w.data.height:
                self.w.data.player.onHit(enemy.hp)
                enemysToRemove.append(enemy)

        for enemy in enemysToRemove:
            enemy.onDeath()

    def stageThreeStart(self):
        pass
    def stageThreeUpdate(self):
        enemysToRemove = []

        for enemy in self.w.data.enemyList:
            enemy.update()
            if enemy.y >= self.w.data.height:
                self.w.data.player.onHit(enemy.hp)
                enemysToRemove.append(enemy)

        for enemy in enemysToRemove:
            enemy.onDeath()



    def stageFourStart(self):
        pass
    def stageFourUpdate(self):
        enemysToRemove = []

        for enemy in self.w.data.enemyList:
            enemy.update()
            if enemy.y >= self.w.data.height:
                self.w.data.player.onHit(enemy.hp)
                enemysToRemove.append(enemy)

        for enemy in enemysToRemove:
            enemy.onDeath()


    def stageFiveStart(self):
        pass
    def stageFiveUpdate(self):
        enemysToRemove = []

        for enemy in self.w.data.enemyList:
            enemy.update()
            if enemy.y >= self.w.data.height:
                self.w.data.player.onHit(enemy.hp)
                enemysToRemove.append(enemy)

        for enemy in enemysToRemove:
            enemy.onDeath()



    def stageSixStart(self):
        pass
    def stageSixUpdate(self):
        enemysToRemove = []

        for enemy in self.w.data.enemyList:
            enemy.update()
            if enemy.y >= self.w.data.height:
                self.w.data.player.onHit(enemy.hp)
                enemysToRemove.append(enemy)

        for enemy in enemysToRemove:
            enemy.onDeath()


    def stageSevenStart(self):
        pass
    def stageSevenUpdate(self):
        enemysToRemove = []

        for enemy in self.w.data.enemyList:
            enemy.update()
            if enemy.y >= self.w.data.height:
                self.w.data.player.onHit(enemy.hp)
                enemysToRemove.append(enemy)

        for enemy in enemysToRemove:
            enemy.onDeath()


    def stageEightStart(self):
        pass
    def stageEightUpdate(self):
        enemysToRemove = []

        for enemy in self.w.data.enemyList:
            enemy.update()
            if enemy.y >= self.w.data.height:
                self.w.data.player.onHit(enemy.hp)
                enemysToRemove.append(enemy)

        for enemy in enemysToRemove:
            enemy.onDeath()


    def stageNineStart(self):
        pass
    def stageNineUpdate(self):
        enemysToRemove = []

        for enemy in self.w.data.enemyList:
            enemy.update()
            if enemy.y >= self.w.data.height:
                self.w.data.player.onHit(enemy.hp)
                enemysToRemove.append(enemy)

        for enemy in enemysToRemove:
            enemy.onDeath()


    def stageTenStart(self):
        pass
    def stageTenUpdate(self):
        enemysToRemove = []

        for enemy in self.w.data.enemyList:
            enemy.update()
            if enemy.y >= self.w.data.height:
                self.w.data.player.onHit(enemy.hp)
                enemysToRemove.append(enemy)

        for enemy in enemysToRemove:
            enemy.onDeath()


