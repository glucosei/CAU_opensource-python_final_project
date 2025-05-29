from main.entity.BaseEntity import BaseEntity
from main.entity.utils import BulletShooter


class BaseEnemy(BaseEntity):
    def __init__(self, w,  x, y, width, height, hp):
        super().__init__(w, x, y, width, height)
        self.MAX_HP = hp
        self.hp = hp
        self.id = w.newRectangle(x,y,width,height, fill_color='red')
        w.data.enemyList.append(self)
        self.bulletShooter = BulletShooter(w, 1, 10, 10)


    def onHit(self, damage):
        self.hp -= damage
        if self.hp<=0:
            self._die()

    def _die(self):
        self.w.deleteObject(self.id)
        self.w.data.enemyList.remove(self)

    def update(self):
        pass

