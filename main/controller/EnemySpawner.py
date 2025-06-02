from main.entity.EnemyTypeA import EnemyTypeA
from main.entity.EnemyTypeB import EnemyTypeB
import random as r

class EnemySpawner:
    def __init__(self, w):
        self.w = w
        self.MAX_ENEMIES = 50
        self.MARGIN = 5

    def _isColliding(self,ax, ay, aw, ah, bx, by, bw, bh):
            return (
                    ax < bx + bw and ax + aw > bx and
                    ay < by + bh and ay + ah > by
            )

    def _findEnemyPosition(self, enemyWidth, enemyHeight):
        if len(self.w.data.enemyList) >= self.MAX_ENEMIES:
            return None

        candidates = []
        y = 0

        for x in range(0, self.w.data.width - enemyWidth, 10):
            overlap = False

            for enemy in self.w.data.enemyList:
                ex, ey = self.w.getPosition(enemy.id)
                ew, eh = self.w.getSize(enemy.id)

                if self._isColliding(
                        x - self.MARGIN, y - self.MARGIN,
                        enemyWidth + 2 * self.MARGIN, enemyHeight + 2 * self.MARGIN,
                        ex, ey, ew, eh
                ):
                    overlap = True
                    break

            if not overlap:
                candidates.append((x, y))

        if candidates:
            return r.choice(candidates)

        return None



    def stageOneSpawn(self):
        for i in range(3):
            result = self._findEnemyPosition(50, 50)
            if result is not None:
                x, y=result
                EnemyTypeA(self.w, x, y)


    def stageTwoSpawn(self):
        for i in range(2):
            result = self._findEnemyPosition(50, 50)
            if result is not None:
                x, y=result
                EnemyTypeA(self.w, x, y)

        for i in range(2):
            result = self._findEnemyPosition(50, 50)
            if result is not None:
                x, y=result
                EnemyTypeB(self.w, x, y)

    def stageThreeSpawn(self):
        pass

    def stageFourSpawn(self):
        pass

    def stageFiveSpawn(self):
        pass

    def stageSixSpawn(self):
        pass

    def stageSevenSpawn(self):
        pass

    def stageEightSpawn(self):
        pass

    def stageNineSpawn(self):
        pass

    def stageTenSpawn(self):
        pass

