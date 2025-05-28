from main.entity.BaseEntity import BaseEntity


class Bullet(BaseEntity):
    def __init__(self, w,  x, y, v, width, height,damage):
        super().__init__(w, x, y, width, height)
        self.damage = damage
        self.id = w.newOval(x,y,width,height, fill_color='red')
        self.v = v
        w.data.bulletList.append(self)



