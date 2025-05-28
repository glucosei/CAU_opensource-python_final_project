from main.entity.BaseEntity import BaseEntity
from main.entity.utils import *


class Player(BaseEntity):



    def __init__(self, w, x, y, width, height, hp, keyboardHandler):
        super().__init__(w, x, y, width, height)
        self.MAX_HP = hp
        self.hp = hp
        self.id = w.newRectangle(x,y,width,height, fill_color='blue')
        self.keyboardHandler = keyboardHandler

        self.da = 0.5/60

        self.vx = 0
        self.vy = 0

        self.ax = 0
        self.ay = 0

        self.shootBullet = ShootBullet(w, -1, 10, 10)

    def onHit(self, damage):
        self.hp -= damage

    def update(self):

        if self.hp <= 0:
            print('dead')

        if self.keyboardHandler.is_pressed('Left'):
            self.ax -= self.da
        if self.keyboardHandler.is_pressed('right'):
            self.ax += self.da
        if self.keyboardHandler.is_pressed('Up'):
            self.ay -= self.da
        if self.keyboardHandler.is_pressed('Down'):
            self.ay += self.da
        if self.keyboardHandler.is_just_released('Left'):
            self.ax = 0
        if self.keyboardHandler.is_just_released('right'):
            self.ax = 0
        if self.keyboardHandler.is_just_released('Up'):
            self.ay = 0
        if self.keyboardHandler.is_just_released('Down'):
            self.ay = 0
        if self.keyboardHandler.is_just_pressed('space'):
            if self.shootBullet.cooldown == 0:
                self.shootBullet.shoot(self.vy,self.x+50, self.y)
                self.shootBullet.cooldown = self.shootBullet.COOLDOWN_TIME


        if self.x < 0 or self.x > 700:
            self.vx -= (7*self.vx)/3
            self.ax = 0
        if self.y < 0 or self.y > 850:
            self.vy -= (7*self.vy)/3
            self.ay = 0

        self.vx += self.ax
        self.vy += self.ay

        self.x, self.y = UpdateLocation.update(self.w, self.id, self.x, self.y, self.vx, self.vy)


        self.vx *= 0.95     #마찰
        self.vy *= 0.95


        if self.shootBullet.cooldown > 0:
            self.shootBullet.cooldown -= 1




