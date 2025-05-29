from main.entity.utils.PositionUpdater import PositionUpdater

class BulletController:
    def __init__(self, w):
        self.w = w

    def update(self):
        for bullet in self.w.data.bulletList:
            PositionUpdater.update(self.w, bullet, 0, bullet.v )

            if bullet.y < -100 or bullet.y > 950:
                self.w.deleteObject(bullet.id)
                self.w.data.bulletList.remove(bullet)
