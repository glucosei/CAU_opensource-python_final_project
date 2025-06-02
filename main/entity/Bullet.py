from main.entity.BaseEntity import BaseEntity


class Bullet(BaseEntity):
    def __init__(self, w,  x, y, vx, vy, width, height,damage, objType):
        super().__init__(w, x, y, width, height)
        self.damage = damage
        self.id = w.newOval(x,y,width,height, fill_color='red')
        self.vx = vx
        self.vy = vy
        w.data.bulletList.append(self)
        self.objType = objType

    def onDeath(self):
        self.w.deleteObject(self.id)
        self.w.data.bulletList.remove(self)


