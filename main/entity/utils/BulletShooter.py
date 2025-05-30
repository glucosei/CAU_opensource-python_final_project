from main.entity.Bullet import Bullet


class BulletShooter:

    def __init__(self, w, heading, damage, speed, cooldownTime=0.1*60):
        """
        heading은 위에서 아래면 1, 아래에서 위면 -1
        """
        self.w = w

        self.heading = heading
        self.bulletList = []
        self.bulletSpeed = speed
        self.cooldown = 0
        self.COOLDOWN_TIME = cooldownTime
        self.damage = damage

    def shoot(self, v0, x, y):
        Bullet(self.w, x, y+30*self.heading, self.heading*self.bulletSpeed+v0, 10, 30, self.damage)

    def isReady(self):
        return self.cooldown <= 0

