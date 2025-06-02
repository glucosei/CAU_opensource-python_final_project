from main.entity.BaseEntity import BaseEntity
from main.entity.utils import *
from main.entity.utils.SkillFlash import SkillFlash


class Player(BaseEntity):



    def __init__(self, w, x, y, width, height, hp):
        super().__init__(w, x, y, width, height)
        self.MAX_HP = hp
        self.hp = hp
        self.id = w.newRectangle(x,y,width,height, fill_color='blue')
        self.keyboardHandler = self.w.data.keyboardHandler

        self.da = 0.5/60

        self.vx = 0
        self.vy = 0

        self.ax = 0
        self.ay = 0

        self.bulletShooter = BulletShooter(w, 10, 0,10, 'p',600/60)
        self.skillFlash = SkillFlash(w,self, 60*1)


        self.playerStatusBar = None

    def onHit(self, damage):
        self.hp = max(self.hp-damage, 0)

    def update(self):
        if self.keyboardHandler.isPressed('Left'):
            self.ax -= self.da
        if self.keyboardHandler.isPressed('right'):
            self.ax += self.da
        if self.keyboardHandler.isPressed('Up'):
            self.ay -= self.da
        if self.keyboardHandler.isPressed('Down'):
            self.ay += self.da
        if self.keyboardHandler.isJustReleased('Left'):
            self.ax = 0
        if self.keyboardHandler.isJustReleased('right'):
            self.ax = 0
        if self.keyboardHandler.isJustReleased('Up'):
            self.ay = 0
        if self.keyboardHandler.isJustReleased('Down'):
            self.ay = 0
        if self.keyboardHandler.isJustPressed('space'):
            if self.bulletShooter.isReady():
                self.bulletShooter.shoot(self.x+self.width/2, self.y, self.vy, -1)
                self.bulletShooter.cooldown = self.bulletShooter.COOLDOWN_TIME

        if self.keyboardHandler.isJustPressed('f'):
            if self.skillFlash.isReady():
                self.skillFlash.flash(self.vx,self.vy)
                self.skillFlash.cooldown = self.skillFlash.COOLDOWN_TIME


        if self.x < 0 or self.x > self.w.data.width-self.width:
            self.vx -= (7*self.vx)/3
            self.ax = 0
        if self.y < 0 or self.y > self.w.data.height-self.height:
            self.vy -= (7*self.vy)/3
            self.ay = 0

        self.vx += self.ax
        self.vy += self.ay

        PositionUpdater.update(self.w, self, self.vx, self.vy)
        self.playerStatusBar.update()



        self.vx *= 0.95     #마찰
        self.vy *= 0.95


        if not self.bulletShooter.isReady():
            self.bulletShooter.cooldown -= 1

        if not self.skillFlash.isReady():
            self.skillFlash.cooldown -= 1




