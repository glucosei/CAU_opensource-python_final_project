from main.entity.BaseEntity import BaseEntity


class BaseEnemy(BaseEntity):
    def __init__(self, w,  x, y, width, height, hp):
        super().__init__(w, x, y, width, height)
        self.MAX_HP = hp
        self.hp = hp
        self.id = w.newRectangle(x,y,width,height, fill_color='red')
        w.data.enemyList.append(self)

    def onHit(self, damage):
        self.hp -= damage


