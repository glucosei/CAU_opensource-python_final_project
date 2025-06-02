from main.entity.BaseEntity import BaseEntity
from main.entity.utils import BulletShooter
from main.ui.HpBar import HpBar


class BaseEnemy(BaseEntity):
    def __init__(self, w,  x, y, width, height, hp):
        super().__init__(w, x, y, width, height)
        self.MAX_HP = hp
        self.hp = hp
        self.id = w.newRectangle(x,y,width,height, fill_color='red')
        self.w.data.enemyList.append(self)
        self.bulletShooter = BulletShooter(w, 10, 0, 10, 'e',12,12, 600/60)

        self.hpBar = HpBar(w, self)
        self.currentHpId = self.hpBar.currentHpId
        self.maxHpId = self.hpBar.maxHpId
        self.w.data.hpBarList.append(self.hpBar)
        self.hpBar = None

    def onHit(self, damage):
        self.hp = max(self.hp-damage, 0)



    def onDeath(self):
        self.w.deleteObject(self.id)
        self.w.data.enemyList.remove(self)
        self.w.deleteObject(self.currentHpId)
        self.w.deleteObject(self.maxHpId)

        self.w.data.hpBarList = [hpBar for hpBar in self.w.data.hpBarList if hpBar.currentHpId != self.currentHpId]

    def update(self):
        pass

