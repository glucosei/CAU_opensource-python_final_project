from main.entity import StageOneEnemy
import random as r

class EnemySpawner:
    def __init__(self, w):
        self.w = w
        self.MAX_ENEMIES = 5
        self.MAX_ATTEMPTS = 100

    def _isColliding(self,ax, ay, aw, ah, bx, by, bw, bh):
            return (
                    ax < bx + bw and ax + aw > bx and
                    ay < by + bh and ay + ah > by
            )

    def _findYZeroEnemyPosition(self, enemy_width, enemy_height, ):
        if len(self.w.data.enemyList) <= self.MAX_ENEMIES:

            overlap = False

            for i in range(self.MAX_ATTEMPTS):
                x = r.randint(0, self.w.data.width - enemy_width)
                y = 0


                for enemy in self.w.data.enemyList:
                    ex, ey = self.w.getPosition(enemy.id)
                    ew, eh = self.w.getSize(enemy.id)

                    if self._isColliding(x, y, enemy_width, enemy_height, ex, ey, ew, eh):
                        overlap = True
                        break

                if not overlap:
                    return x, y  # 겹치지 않으면 위치 반환

        return None  # 실패 시 None 반환


    def stageOneSpawn(self):
        result = self._findYZeroEnemyPosition(100, 100)
        if result is not None:
            x, y=result
            StageOneEnemy(self.w, x, y)

