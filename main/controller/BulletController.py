from main.entity.utils.UpdateLocation import UpdateLocation

class BulletController:
    def __init__(self, w):
        self.w = w

    def update(self):
        for bullet in self.w.data.bulletList:
            bullet.x, bullet.y = UpdateLocation.update(self.w,bullet.id, bullet.x, bullet.y, 0, bullet.v )

            if bullet.y < -100 or bullet.y > 950:
                self.w.deleteObject(bullet.id)
                self.w.data.bulletList.remove(bullet)
