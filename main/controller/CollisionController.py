class CollisionController:
    def __init__(self, w, player):
        self.w = w
        self.player = player

    @staticmethod
    def _isColliding(ax, ay, aw, ah, bx, by, bw, bh):
        return (
                ax < bx + bw and ax + aw > bx and
                ay < by + bh and ay + ah > by
        )




    def update(self):
        px, py = self.w.getPosition(self.player.id)
        pw, ph = self.w.getSize(self.player.id)
        for bullet in self.w.data.bulletList:

            bx, by = self.w.getPosition(bullet.id)
            bw, bh = self.w.getSize(bullet.id)

            for enemy in self.w.data.enemyList:
                ex, ey = self.w.getPosition(enemy.id)
                ew, eh = self.w.getSize(enemy.id)

                if self._isColliding(bx, by, bw, bh, ex, ey, ew, eh):
                    enemy.onHit(bullet.damage)
                    self.w.deleteObject(bullet.id)
                    self.w.data.bulletList.remove(bullet)

            if self._isColliding(bx, by, bw, bh, px, py, pw, ph):
                self.player.onHit(bullet.damage)
                self.w.deleteObject(bullet.id)
                self.w.data.bulletList.remove(bullet)
