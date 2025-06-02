from main.entity.Bullet import Bullet


class BulletShooter:

    def __init__(self, w, damage, speedX, speedY, objType, cooldownTime=0.1*60):
        """
        heading은 위에서 아래면 1, 아래에서 위면 -1
        """
        self.w = w

        self.bulletList = []
        self.bulletSpeedX = speedX
        self.bulletSpeedY = speedY
        self.cooldown = 0
        self.COOLDOWN_TIME = cooldownTime
        self.damage = damage
        self.objType = objType

    def shoot(self, x, y, vy0, heading):
        Bullet(self.w, x, y+10*heading,self.bulletSpeedX, heading*max(self.bulletSpeedY, (self.bulletSpeedY+vy0*heading)), 6, 12, self.damage, self.objType)

    def isReady(self):
        return self.cooldown <= 0

